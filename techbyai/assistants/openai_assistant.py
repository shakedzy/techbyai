import json
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI, BadRequestError
from openai.types.chat import ChatCompletion, ChatCompletionMessage, ChatCompletionMessageToolCall
from openai._types import NOT_GIVEN
from typing import Any, Callable
from .base_assistant import BaseAssistant
from ..settings import Settings
from ..tools import tools_params_definitions, REQUIRED_PARAM
from ..archive import Archive
from ..constants import TOOL_CALLS


class OpenAIAssistant(BaseAssistant):
    def __init__(self, definition: str, client: OpenAI, *, tools: list[Callable] = [], name: str | None = None, archive: Archive | None = None) -> None:
        super().__init__(definition, name=name, archive=archive)
        self.client = client
        self.tools = self._build_tools(tools) if tools else NOT_GIVEN

    def _build_tools(self, functions: list[Callable]) -> list[dict[str, Any]]:
        tools = list()
        tools_params = tools_params_definitions()
        for func in set(functions):
            v = tools_params.get(func, [])
            params = {}
            required = []
            for p in v:
                params[p[0]] = p[1]
                if p[2] == REQUIRED_PARAM: 
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
        input_tokens: int = completion.usage.prompt_tokens       # type: ignore
        output_tokens: int = completion.usage.completion_tokens  # type: ignore
        self.cost.add('input_tokens', input_tokens)
        self.cost.add('output_tokens', output_tokens)

    def _chat_assistant_message_to_dict(self, completion_message: ChatCompletionMessage) -> dict[str, Any]:
        message = dict()
        message['role'] = completion_message.role
        message['content'] = completion_message.content
        if completion_message.tool_calls:
            message[TOOL_CALLS] = completion_message.tool_calls
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
                "role": self.tool_role,
                "name": tool_name,
                "content": tool_result
            }
        else:
            self.logger.warn(f"Model requested non-existing tool: {tool_name}, skipping", color='yellow')
            return None
        
    def _handle_tools(self, messages: list[dict[str, Any]], tool_calls: list) -> tuple[list[dict[str, Any]], bool]:
        tools_messages = []
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._run_tool_call, tool_call) for tool_call in tool_calls]
        for result in [f.result() for f in futures]:
            if result:
                tools_messages.append(result)
        return messages + tools_messages, bool(tools_messages)
        
    def _get_completion_message(self, as_json: bool, messages: list[dict[str, Any]], additional_temperature: float) -> dict[str, Any]:
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
    