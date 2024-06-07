import json
from dataclasses import dataclass, field
from datetime import datetime
from openai import OpenAI, BadRequestError
from openai.types.chat import ChatCompletion
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
        """
        Initializes a `Client` object with various parameters such as client,
        definition, name, tools, callables, logger, cost, and archive.

        Args:
            definition (str): code's documentation.
            tools ([]): set of tools that are used to generate the code documentation,
                and it is used to construct the `build_tools()` function that
                creates the callables for the client's API.
            name (None): name of the module or package that contains the code to
                be documented.
            archive (None): archive  to which the code generator will write its
                documentation, ensuring that it is properly stored and organized.

        """
        self.client = OpenAI()
        self.definition = definition
        self.name = name
        self.tools = build_tools(tools) if tools else NOT_GIVEN
        self.callables = {f.__name__: f for f in tools}
        self.logger = get_logger()
        self.cost = Cost()
        self.archive = archive 

    def _compute_cost(self, completion: ChatCompletion) -> None:
        """
        Computes the cost for a given prompt and completion tokens, adding them
        to the `self.cost` dict accordingly.

        Args:
            completion (ChatCompletion): prompt tokens for which the completion
                is being generated.

        """
        input_tokens: int = completion.usage.prompt_tokens      # type: ignore
        output_tokens: int = completion.usage.completion_tokens  # type: ignore
        self.cost.add('input_tokens', input_tokens)
        self.cost.add('output_tokens', output_tokens)

    def _summarize_conversation(self, conversation: list[dict[str, str]]) -> list[dict[str, str]]:
        """
        Summarizes a given conversation by identifying and limiting the number of
        words in each message, then grouping them into categories and returning
        the summaries.

        Args:
            conversation (list[dict[str, str]]): sequence of messages that needs
                to be summarized using the given code.

        Returns:
            list[dict[str, str]]: a list of summarized messages, where each message
            contains a role and a content that has been condensed to a maximum of
            3000 words.

        """
        MAX_WORDS = 3000
        self.logger.debug("Summarizing conversation...")

        summarized = []
        count = 0
        for i, message in enumerate(conversation, start=1):
            num_words = len([word for word in message['content'].split(' ') if word.strip()])
            self.logger.debug(f'Message {i} by {message['role']} contains {num_words} words')
            if num_words > MAX_WORDS:
                s_content = self.do(f"Summarize the text below to no more than {MAX_WORDS}:\n-----\n{message['content']}")
                count += 1
                summarized.append({"role": message["role"], "content": s_content})
            else:
                summarized.append(message)
        self.logger.debug(f"Summarized {count} messages")
        return summarized
    
    def do(self, task: str, *, as_json: bool = False, conversation: list = [], _summarize_conversation: bool = False) -> AssistantResponse:
        """
        Is an API endpoint that takes a task, as JSON input, and responds with a
        JSON output, based on a series of interactions with a language model client.
        It creates and sends a completion request to the model, analyzes the
        response, and generates a reply.

        Args:
            task (str): user's task or question that the AI assistant is trying
                to answer.
            as_json (False): whether the response should be formatted as JSON
            conversation ([]): 3-4 previous messages in the conversation and is
                used to generate the assistant's response based on the context of
                the conversation.
            _summarize_conversation (False): conversation and system prompts are
                summarized at each iteration of the `for` loop, creating a condensed
                version of the dialogue for further processing.

        Returns:
            AssistantResponse: an Assistant Response containing the result of the
            given task.

        """
        if _summarize_conversation:
            conversation = self._summarize_conversation(conversation)
        
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
                    return self.do(task=task, as_json=as_json, conversation=conversation, _summarize_conversation=True)
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
            assistant_message = completion.choices[0].message  # type: ignore
            messages.append(assistant_message)                 # type: ignore
            self._compute_cost(completion)
            
            if assistant_message.tool_calls:
                hallucination_indices: list[int] = []
                for i, tool_call in enumerate(assistant_message.tool_calls):
                    tool_name = tool_call.function.name

                    if tool_name == "multi_tool_use.parallel":
                        # This is a tool hallucination by GPT, it does not exist
                        hallucination_indices.append(i)
                        self.logger.info("Got hallucination tool request")
                        continue

                    arguments = json.loads(tool_call.function.arguments)
                    if tool_name == 'query_magazine_archive':
                        arguments['archive'] = self.archive
                    self.logger.info(f"Running tool {tool_name}: {str(arguments)}", color='yellow')
                    tool_result = self.callables[tool_name](**arguments)
                    
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": tool_name,
                        "content": tool_result
                    })
                
                if hallucination_indices:
                    for i in hallucination_indices:
                        # Remove hallucination-tool calls, as if it never happened
                        assistant_message.tool_calls.pop(i)
                    
                    if not assistant_message.tool_calls:
                        # All tool calls were hallucinations
                        messages.pop()  # remove the last message (as it is now just an empty list of tool calls, no tools were called)
                        additional_temperature = .3  # increase temperature momentarily to avoid creating the same message again

            elif as_json:
                try:
                    content: str = messages[-1].content  # type: ignore
                    content_json = json.loads(content)
                    final_message = True
                except Exception as e:
                    self.logger.warn(f"Error decoding message as JSON - {e.__class__.__name__}: {e}", color='red')
                    messages.append({
                        "role": "user",
                        "content": "The message is not formatted as a valid JSON! Return it as a valid JSON according to the format you were given"
                    })
            else:
                content = messages[-1].content  # type: ignore
                content_json = {}
                final_message = True
        
        messages.pop(0)  # remove system prompt
        return AssistantResponse(content=content, json=content_json, conversation=messages)
    