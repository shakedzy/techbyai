import json

from openai import OpenAI, BadRequestError
from openai.types.chat import ChatCompletion, ChatCompletionMessage, ChatCompletionMessageToolCall
from openai._types import NOT_GIVEN
from pydantic import BaseModel, RootModel, ValidationError
from typing import Any, Callable, Type
from .base_assistant import BaseAssistant, AssistantResponse
from ..settings import Settings
from ..tools import TOOLS_PARAMS_DEFINITIONS
from ..archive import Archive


class OpenAIAssistant(BaseAssistant):
    def __init__(self, definition: str, client: OpenAI, *, tools: list[Callable] = [], name: str | None = None, archive: Archive | None = None) -> None:
        super().__init__(definition, name=name, archive=archive)
        self.client = client
        self.tools = self._build_tools(tools) if tools else NOT_GIVEN

    def _build_tools(self, functions: list[Callable]) -> list[dict[str, Any]]:
        tools = list()
        for func in set(functions):
            v = TOOLS_PARAMS_DEFINITIONS.get(func, [])
            params = {}
            required = []
            for p in v:
                params[p[0]] = p[1]
                if p[2]: 
                    required.append(p[0])

            tools.append({
                "type": "function",
                "function": {
                    "name": func.__name__,
                    "description": func.__doc__,
                    "parameters": {
                        "type": "object",
                        "properties": params
                    },
                    "required": required
                }
            })
        return tools

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
        
    def _get_completion_message(self, as_json: bool, messages: list[dict[str, str]], additional_temperature: float) -> dict[str, Any]:
            try:
                completion = self.client.chat.completions.create(
                    model=Settings().llm.model, 
                    temperature=Settings().llm.temperature + additional_temperature, 
                    messages=messages,  # type: ignore
                    tools=self.tools,   # type: ignore
                    response_format={"type": "json_object"} if as_json else NOT_GIVEN
                )
            except BadRequestError as e:
                try:
                    messages = self._summarize_conversation(messages)
                    completion = self.client.chat.completions.create(
                        model=Settings().llm.model, 
                        temperature=Settings().llm.temperature + additional_temperature, 
                        messages=messages,  # type: ignore  
                        tools=self.tools,   # type: ignore
                        response_format={"type": "json_object"} if as_json else NOT_GIVEN
                    )
                except Exception as e:
                    raise e
            self._compute_cost(completion)
            return self._chat_assistant_message_to_dict(completion.choices[0].message)
