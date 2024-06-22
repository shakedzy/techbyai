import json
import ollama
from paramiko.client import SSHClient
from typing import Any, Callable
from .base_assistant import BaseAssistant, AssistantResponse
from ..settings import Settings
from ..tools import tools_params_definitions, REQUIRED_PARAM
from ..archive import Archive
from ..utils import dedent


class OllamaAssistant(BaseAssistant):
    def __init__(self, definition: str, client: SSHClient | None, *, tools: list[Callable] = [], name: str | None = None, archive: Archive | None = None) -> None:
        super().__init__(definition, name=name, archive=archive)
        self.client = client
        self.tools = self._build_tools(tools) if tools else None

    def _build_tools(self, functions: list[Callable]) -> list[str]:
        tools = list()
        tools_params = tools_params_definitions()
        match Settings().llm.type:
            case "cohere":
                for func in set(functions):
                    v = tools_params.get(func, [])
                    signature_params = []
                    docstring_params = []
                    for p in v:
                        sp = f"{p[0]}: {p[1]['type']}"
                        dp = f"{p[0]} ({p[1]['type']}): {p[1]['description']}"
                        if p[2] != REQUIRED_PARAM:
                            sp += f" = {p[2]}"
                        signature_params.append(sp)
                        docstring_params.append(dp)
                    f = dedent(
                        f'''
                        ```python
                        def {func.__name__}({', '.join(signature_params)}) -> List[Dict]:
                            """
                            {func.__doc__}
                            Args:
                                {'\n\t'.join(docstring_params)}
                            """
                            pass 
                        ```
                        '''
                    )
                    tools.append(f)
                tools.append(dedent(
                    '''
                    ```python
                    def directly_answer() -> List[Dict]:
                        """
                        Calls a standard (un-augmented) AI chatbot to generate a response given the conversation history
                        """
                        pass
                    ```
                    '''
                ))
            case _:
                raise ValueError(f"{Settings().llm.type} is not supported")
        return tools
    
    def _get_command_r_prompt(self, messages: list[dict[str, str]]) -> str:
        # See Cohere's documentation here: https://docs.cohere.com/docs/prompting-command-r
        pass

    def _get_raw_ollama_completion(self, prompt: str, *, as_json: bool, additional_temperature: float) -> str:
        match type(self.client):
            case None:
                response = ollama.generate(
                    model=Settings().llm.model,
                    prompt=prompt,
                    raw=True,
                    stream=False,
                    format='json' if as_json else '',
                    options={
                        'temperature': Settings().llm.temperature + additional_temperature
                    }
                )
                content: str = response['response']  # type: ignore
            
            case SSHClient:
                content = ''

        return content
    
    def _get_completion_message(self, as_json: bool, messages: list[dict[str, str]], additional_temperature: float) -> dict[str, Any]:
        match Settings().llm.model:
            case 'command-r' | 'command-r-plus':
                prompt = self._get_command_r_prompt(messages)
                content = self._get_raw_ollama_completion(prompt, as_json=as_json, additional_temperature=additional_temperature)
                if content.startswith('Action:'):
                    # Tool calling
                    pass
                else:
                    return {
                        "role": self.assistant_role,
                        "content": content
                    }
            case _:
                raise ValueError(f"{type(self.client)} with {Settings().llm.type} is not supported")
