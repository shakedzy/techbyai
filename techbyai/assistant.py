import json
from datetime import datetime
from openai import OpenAI
from openai.types.chat import ChatCompletion
from openai._types import NOT_GIVEN
from typing import Any
from .settings import Settings
from .tools import tools_params_definitions
from .color_logger import get_logger


class Assistant:
    def __init__(self, definition: str, name: str) -> None:
        self.client = OpenAI()
        self.definition = definition
        self.name = name
        self.tools = self._build_tools()
        self.callables = {f.__name__: f for f in tools_params_definitions.keys()}
        self.logger = get_logger()

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

    def _compute_cost(self, completion: ChatCompletion) -> float:
        prompt_tokens: int = completion.usage.prompt_tokens      # type: ignore
        output_tokens: int = completion.usage.completion_tokens  # type: ignore
        return (prompt_tokens * Settings().llm.input_costs_per_mill + output_tokens * Settings().llm.output_costs_per_mill) / 1e6
    
    def do(self, task: str, as_json: bool = False) -> dict[str, Any]:
        system_prompt = f"[Today is {datetime.now().strftime('%d %B, %Y')}{', your name is '+self.name if self.name else ''}]\n{self.definition}"
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": task}
        ]
        cost = 0.

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
            cost += self._compute_cost(completion)
            
            if assistant_message.tool_calls:
                for tool_call in assistant_message.tool_calls:
                    tool_name = tool_call.function.name
                    arguments = json.loads(tool_call.function.arguments)
                    self.logger.info(f"Running tool {tool_name}: {str(arguments)}", color='yellow')
                    tool_result = self.callables[tool_name](**arguments)
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": tool_name,
                        "content": tool_result
                    })
            else:
                final_message = True

        return {
            'response': messages[-1].content,  # type: ignore
            'cost': cost
        } 
    