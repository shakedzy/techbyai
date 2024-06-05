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
        Sets up instance variables `client`, `definition`, `name`, `tools`,
        `callables`, `logger`, `cost`, and `archive`. It also calls `build_tools()`
        if the `tools` parameter is given, and provides default values for any
        missing parameters.

        Args:
            definition (str): definition of a code module or package to be generated,
                which is used by the OpenAI API to generate high-quality documentation
                for the given code.
            tools ([]): list of tools to be used for building the client, which
                is used to construct the `build_tools` function that creates a
                dictionary of callables for the client.
            name (None): name of the generated code, which is assigned to the
                instance attribute `name` upon initialization.
            archive (None): dataset or file that contains the examples to be used
                for training and evaluation.

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
        Computes the cost for a given prompt based on the number of input and
        output tokens required to generate the completion suggestions.

        Args:
            completion (ChatCompletion): usage of the completion interface, providing
                the number of prompt tokens and completion tokens required for
                cost calculation.

        """
        input_tokens: int = completion.usage.prompt_tokens      # type: ignore
        output_tokens: int = completion.usage.completion_tokens  # type: ignore
        self.cost.add('input_tokens', input_tokens)
        self.cost.add('output_tokens', output_tokens)

    def _summarize_conversation(self, conversation: list[dict[str, str]]) -> list[dict[str, str]]:
        """
        Takes a conversation and outputs a list of summary messages, each containing
        information on the message's role and a concise version of the original text.

        Args:
            conversation (list[dict[str, str]]): conversation or dialogue to be
                summarized by the function.

        Returns:
            list[dict[str, str]]: a list of dictionaries, where each dictionary
            represents a message in the conversation and contains information on
            the message's role and a summary of its content.

        """
        MAX_WORDS = 3000
        self.logger.debug("Summarizing conversation...")

        summarized = []
        count = 0
        for message in conversation:
            num_words = len([word for word in message['content'].split(' ') if word.strip()])
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
        Takes a task and a list of messages as input and returns an assistant
        response. It executes a chatbot dialogue using the client API, processing
        the user's input, generating responses, and updating the conversation.

        Args:
            task (str): task or goal that the user wants to accomplish, and it is
                used as the initial message to trigger the dialogue with the assistant.
            as_json (False): JSON format for the output message, where it is True
                (or set to True), the assistant responds with the entire conversation
                as a JSON object; otherwise, only the final message will be returned
                as JSON.
            conversation ([]): pre-processed chatlog to be passed through the GPT
                model, and it is used to train the model and generate responses
                based on the input context provided.
            _summarize_conversation (False): 0-based index of the last user message
                that should be included in the response, effectively summarizing
                the conversation before generating the final response.

        Returns:
            AssistantResponse: an Assistant response containing the user's message
            and the generated response.

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
    