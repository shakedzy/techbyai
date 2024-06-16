import json
from dataclasses import dataclass, field
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI, BadRequestError
from openai.types.chat import ChatCompletion, ChatCompletionMessage, ChatCompletionMessageToolCall
from openai._types import NOT_GIVEN
from typing import Any, Callable
from .cost import Cost
from .settings import Settings
from .tools import build_tools
from .color_logger import get_logger
from .archive import Archive


@dataclass
class AssistantResponse:
    content: str
    json: dict[str, Any]
    conversation: list = field(default_factory=list)


class Assistant:
    def __init__(self, definition: str, *, tools: list[Callable] = [], name: str | None = None, archive: Archive | None = None) -> None:
        self.client = OpenAI()
        self.definition = definition
        self.name = name
        self.tools = build_tools(tools) if tools else NOT_GIVEN
        self.callables = {f.__name__: f for f in tools}
        self.logger = get_logger()
        self.cost = Cost()
        self.archive = archive 

    def _compute_cost(self, completion: ChatCompletion) -> None:
        input_tokens: int = completion.usage.prompt_tokens      # type: ignore
        output_tokens: int = completion.usage.completion_tokens  # type: ignore
        self.cost.add('input_tokens', input_tokens)
        self.cost.add('output_tokens', output_tokens)

    def _chat_assistant_message_to_dict(self, completion_message: ChatCompletionMessage) -> dict[str, Any]:
        message = dict()
        message['role'] = completion_message.role
        message['content'] = completion_message.content
        if completion_message.tool_calls:
            message['tool_calls'] = completion_message.tool_calls
        return message

    def _summarize_conversation(self, conversation: list[dict[str, str]]) -> list[dict[str, str]]:
        MAX_WORDS = 3000
        self.logger.debug("Summarizing conversation...", color='cyan')
        summarized = []
        count = 0
        for i, message in enumerate(conversation, start=1):
            content: str = message['content'] or ''
            num_words = len([word for word in content.split(' ') if word.strip()])
            self.logger.debug(f"Message {i} by {message['role']} contains {num_words} words")
            if num_words > MAX_WORDS:
                s_content = self.do(f"Summarize the text below to no more than {MAX_WORDS}:\n-----\n{message['content']}")
                count += 1
                summarized.append({"role": message["role"], "content": s_content})
            else:
                summarized.append(message)
        self.logger.debug(f"Summarized {count} messages")
        return summarized
    
    def _run_tool_call(self, tool_call: ChatCompletionMessageToolCall) -> dict[str, str] | None:
        tool_name = tool_call.function.name
        if tool_name in self.callables:
            arguments = json.loads(tool_call.function.arguments)
            if tool_name == 'query_magazine_archive':
                arguments['archive'] = self.archive
            self.logger.info(f"Running tool {tool_name}: {str(arguments)}", color='yellow')
            tool_result = self.callables[tool_name](**arguments)
            return {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": tool_name,
                "content": tool_result
            }
        else:
            self.logger.warn(f"Model requested non-existing tool: {tool_name}, skipping", color='yellow')
            return None
    
    def do(self, task: str, *, as_json: bool = False, conversation: list = [], _summarize_conversation: bool = False) -> AssistantResponse:
        if _summarize_conversation:
            messages = self._summarize_conversation(conversation)
        
        else:
            system_prompt = f"[Today is {datetime.now().strftime('%d %B, %Y')}{', your name is ' + self.name if self.name else ''}]\n{self.definition}"
            messages = [
                {"role": "system", "content": system_prompt}
                ] + conversation + [
                {"role": "user", "content": task}
            ]

        final_message = False
        additional_temperature: float = 0.0
        while not final_message:
            try:
                completion = self.client.chat.completions.create(
                    model=Settings().llm.model, 
                    temperature=Settings().llm.temperature + additional_temperature, 
                    messages=messages,  # type: ignore
                    tools=self.tools,   # type: ignore
                    response_format={"type": "json_object"} if as_json else NOT_GIVEN
                )
            except BadRequestError as e:
                if not _summarize_conversation:
                    return self.do(task=task, as_json=as_json, conversation=messages, _summarize_conversation=True)
                else:
                    raise e
            except Exception as e:
                error_message = f'ERROR - {e.__class__.__name__}: {e}'
                if as_json:
                    json_error_message = {"error": error_message}
                    error_message = json.dumps(json_error_message)
                else:
                    json_error_message = {}
                messages.append({
                    "role": "assistant",
                    "content": error_message
                })
                return AssistantResponse(content=error_message, json=json_error_message, conversation=messages)

            additional_temperature = 0.0
            assistant_message = completion.choices[0].message  
            messages.append(self._chat_assistant_message_to_dict(assistant_message))                 
            self._compute_cost(completion)
            
            if assistant_message.tool_calls:
                succeeded_any_tool_call = False
                with ThreadPoolExecutor() as executor:
                    futures = [executor.submit(self._run_tool_call, tool_call) for tool_call in assistant_message.tool_calls]
                for result in [f.result() for f in futures]:
                    if result:
                        succeeded_any_tool_call = True
                        messages.append(result)
                if not succeeded_any_tool_call:
                    # All tool calls were hallucinations. This is a super rare case.
                    messages.pop()  # remove the last message (this the assistant message, asking for non-existing tools)
                    additional_temperature = .3  # increase temperature momentarily to avoid creating the same message again
                    self.logger.warn("All tool-calls were hallucinations, increasing temperature and retrying", color="red")
                        
            elif as_json:
                try:
                    content: str = assistant_message.content or ''
                    content_json = json.loads(content)
                    final_message = True
                except Exception as e:
                    self.logger.warn(f"Error decoding message as JSON - {e.__class__.__name__}: {e}", color='red')
                    messages.append({
                        "role": "user",
                        "content": "The message is not formatted as a valid JSON! Return it as a valid JSON according to the format you were given"
                    })
            else:
                content = assistant_message.content or ''
                content_json = {}
                final_message = True
        
        messages.pop(0)  # remove system prompt
        return AssistantResponse(content=content, json=content_json, conversation=messages)
    