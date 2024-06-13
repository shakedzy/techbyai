import re
import json
import cohere
from cohere.base_client import OMIT
from cohere.types.non_streamed_chat_response import NonStreamedChatResponse
from datetime import datetime
from typing import Callable, Any
from .base import Assistant, AssistantResponse
from ..settings import Settings
from ..archive import Archive
from ..tools import TOOLS_PARAMS_DEFINITIONS


class CohereAssistant(Assistant):
    def __init__(self, definition: str, *, tools: list[Callable] = [], name: str | None = None, archive: Archive | None = None) -> None:
        super().__init__(definition, tools=tools, name=name, archive=archive)
        self.client = cohere.Client()
        self.tools = self._build_tools(tools) if tools else OMIT

    @staticmethod
    def _build_tools(functions: list[Callable]) -> list[dict[str, Any]]:
        tools = list()
        for func in set(functions):
            v = TOOLS_PARAMS_DEFINITIONS["cohere"].get(func, [])
            params = {}
            for p in v:
                params[p[0]] = {
                    "type": p[1]["type"],
                    "description": p[1]["description"],
                    "required": p[2]
                }
            tools.append({
                "name": func.__name__,
                "description": func.__doc__,
                "parameter_definitions": params,
            })
        return tools
    
    @staticmethod
    def _extract_json_from_string(text: str) -> str:
        pattern = r'```json\s*([\s\S]*?)\s*```'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            return match.group(1)
        return text
    
    def _summarize_conversation(self, conversation: list[dict[str, str]]) -> list[dict[str, str]]:
        return conversation

    def _compute_cost(self, completion: NonStreamedChatResponse) -> None:
        input_tokens: int = int(completion.meta.tokens.input_tokens)    # type: ignore
        output_tokens: int = int(completion.meta.tokens.output_tokens)  # type: ignore
        self.cost.add('input_tokens', input_tokens)
        self.cost.add('output_tokens', output_tokens)

    def do(self, task: str, *, as_json: bool = False, conversation: list = [], _summarize_conversation: bool = False) -> AssistantResponse:
        system_prompt = f"[Today is {datetime.now().strftime('%d %B, %Y')}{', your name is ' + self.name if self.name else ''}]\n{self.definition}"
        if _summarize_conversation:
            messages = self._summarize_conversation(conversation)
        else:
            messages = conversation

        final_message = False
        additional_temperature: float = 0.0
        tool_results = []
        while not final_message:
            try:
                completion = self.client.chat(
                    model=Settings().llm.model, 
                    temperature=Settings().llm.temperature + additional_temperature, 
                    message=task if not tool_results else "",
                    preamble=system_prompt,
                    chat_history=messages,  # type: ignore
                    tools=self.tools,       # type: ignore
                    tool_results=tool_results or OMIT
                )
                tool_results = []
            except Exception as e:
                error_message = f'ERROR - {e.__class__.__name__}: {e}'
                print(task)
                print(system_prompt)
                print(bool(tool_results))
                if as_json:
                    json_error_message = {"error": error_message}
                    error_message = json.dumps(json_error_message)
                else:
                    json_error_message = {}
                messages.append({
                    "role": "CHATBOT",
                    "message": error_message
                })
                return AssistantResponse(content=error_message, json=json_error_message, conversation=messages)

            additional_temperature = 0.0
            messages = [m.dict() for m in completion.chat_history or list()]
            self._compute_cost(completion)
            
            if completion.tool_calls:
                for tool_call in completion.tool_calls:
                    tool_name = tool_call.name
                    arguments = tool_call.parameters
                    if tool_name == 'query_magazine_archive':
                        arguments['archive'] = self.archive
                    self.logger.info(f"Running tool {tool_name}: {str(arguments)}", color='yellow')
                    tool_results.append(
                        {
                            "call": {
                                "name": tool_call.name,
                                "arguments": {k: v for k,v in arguments.items() if k != 'archive'},
                            },
                            "output":
                                [{
                                    "output": self.callables[tool_name](**arguments)
                                }]
                        }
                    )
                    
            elif as_json:
                try:
                    content: str = completion.text
                    content_json = json.loads(self._extract_json_from_string(content))
                    final_message = True
                except Exception as e:
                    self.logger.warn(f"Error decoding message as JSON - {e.__class__.__name__}: {e}", color='red')
                    self.logger.debug(f"Original message:\n{content}", color='red')
                    self.logger.debug(f"Extracted:\n{self._extract_json_from_string(content)}")
                    messages.append({
                        "role": "USER",
                        "message": "The message is not formatted as a valid JSON! Return it as a valid JSON according to the format you were given"
                    })
            else:
                content = completion.text
                content_json = {}
                final_message = True
        
        return AssistantResponse(content=content, json=content_json, conversation=messages)
    