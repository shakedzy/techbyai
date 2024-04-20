import json
from dataclasses import dataclass, field
from datetime import datetime
from openai import OpenAI
from openai.types.chat import ChatCompletion
from openai._types import NOT_GIVEN
from typing import Any
from .cost import Cost
from .settings import Settings
from .tools import tools_params_definitions
from .color_logger import get_logger
from .archive import Archive


@dataclass
class AssistantResponse:
    content: str
    json: dict[str, Any]
    conversation: list = field(default_factory=list)


class Assistant:
    def __init__(self, definition: str, *, name: str, archive: Archive) -> None:
        self.client = OpenAI()
        self.definition = definition
        self.name = name
        self.tools = self._build_tools()
        self.callables = {f.__name__: f for f in tools_params_definitions.keys()}
        self.logger = get_logger()
        self.cost = Cost()
        self.archive = archive

    def _build_tools(self) -> list[dict[str, Any]]:
        tools = list()
        for func, v in tools_params_definitions.items():
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
        prompt_tokens: int = completion.usage.prompt_tokens      # type: ignore
        output_tokens: int = completion.usage.completion_tokens  # type: ignore
        current_cost = (prompt_tokens * Settings().llm.input_costs_per_mill + output_tokens * Settings().llm.output_costs_per_mill) / 1e6
        self.cost += current_cost
    
    def do(self, task: str, *, as_json: bool = False, conversation: list = []) -> AssistantResponse:
        system_prompt = f"[Today is {datetime.now().strftime('%d %B, %Y')}{', your name is ' + self.name if self.name else ''}]\n{self.definition}"
        messages = [
            {"role": "system", "content": system_prompt}
            ] + conversation + [
            {"role": "user", "content": task}
        ]

        final_message = False
        while not final_message:
            completion = self.client.chat.completions.create(
                model=Settings().llm.model, 
                temperature=Settings().llm.temperature, 
                messages=messages,  # type: ignore
                tools=self.tools,   # type: ignore
                response_format={"type": "json_object"} if as_json else NOT_GIVEN
            )
            assistant_message = completion.choices[0].message
            messages.append(assistant_message)  # type: ignore
            self._compute_cost(completion)
            
            if assistant_message.tool_calls:
                for tool_call in assistant_message.tool_calls:
                    tool_name = tool_call.function.name
                    if tool_name == "multi_tool_use.parallel":
                        # This is a tool hallucination by GPT, it does not exist
                        tool_name = "multi_tool_use_parallel"  # match '^[a-zA-Z0-9_-]{1,64}$'
                        tool_result = "There's no such tool names `multi_tool_use.parallel`, use the correct syntax to call multiple tools!"
                    else:
                        arguments = json.loads(tool_call.function.arguments)
                        if tool_name == 'query_magazine_archive':
                            arguments['archive'] = self.archive
                        self.logger.info(f"Running tool {tool_name}: {str(arguments)}", color='yellow')
                        tool_result = self.callables[tool_name](**arguments)
                        if tool_name == 'web_search':
                            self.cost += Settings().search.cost_per_query
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": tool_name,
                        "content": tool_result
                    })
            elif as_json:
                try:
                    content: str = messages[-1].content  # type: ignore
                    content_json = json.loads(content)
                    final_message = True
                except Exception as e:
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
    