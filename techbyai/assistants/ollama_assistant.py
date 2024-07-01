import json
import ollama
from concurrent.futures import ThreadPoolExecutor
from paramiko.client import SSHClient
from typing import Any, Callable
from .base_assistant import BaseAssistant
from ..settings import Settings
from ..tools import tools_params_definitions, REQUIRED_PARAM
from ..archive import Archive
from ..utils import dedent, lowercase_keys
from ..schemas import OllamaToolsCall
from ..constants import DIRECTLY_ANSWER_TOOL, DIRECTLY_ANSWER_TOOL_RESPONSE, TOOL_CALLS


class OllamaAssistant(BaseAssistant):
    # Designed to be used with Cohere's Command-R and Command-R+ models

    def __init__(self, definition: str, client: SSHClient | None, *, tools: list[Callable] = [], name: str | None = None, archive: Archive | None = None) -> None:
        super().__init__(definition, name=name, tools=tools, archive=archive)
        self.client = client
        self.tools = self._build_tools(tools) if tools else None

    def _build_tools(self, functions: list[Callable]) -> list[str]:
        # Based on: https://docs.cohere.com/docs/prompting-command-r
        tools = list()
        tools_params = tools_params_definitions()
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
                def {func.__name__}({', '.join(signature_params)}) -> str:
                    """
                    {func.__doc__}
                    Args:
                        {'\n\t'.join(docstring_params)}
                    """
                    pass 
                '''
            )
            tools.append(f)
        tools.append(dedent(
            f'''
            def {DIRECTLY_ANSWER_TOOL}({DIRECTLY_ANSWER_TOOL_RESPONSE}: str) -> str:
                """
                Calls a standard (un-augmented) AI chatbot to generate a response given the conversation history
                Use this tool when you want to directly answer a question without using any other tools.
                Args:
                    response (str): The response to be answered
                """
                pass
            '''
        ))
        return tools
    
    def get_system_prompt(self) -> str:
        base_system_prompt = super().get_system_prompt()
        if not self.tools:
            return base_system_prompt
        system_prompt = dedent(
            f"""
            {base_system_prompt}
            
            You are provided with the following list of tools, given to you as signatures of Python functions.
            When replying, you may choose one or more tools to use in order to get more relevant information before answering.
            If you choose to use a tool, you must reply with in the following JSON format:
            ```json
            {{
                "tools": 
                    [
                        {{
                            "tool": "TOOL_NAME",
                            "parameters": 
                                {{
                                    "PARAMETER": "VALUE", 
                                    ...
                                }}
                        }},
                        ...
                    ]
            }}
            ```
            If you choose to use tools, do not add anything other than the JSON. You MUST use the EXACT format in case you do!
            If a tool doesn't accept any parameters, the value of the "parameters" key must by an empty dictionary.
            You may use the `directly_answer` tool to directly answer a question without using any other tools. If you choose this, 
            you may not call any other tool with it.

            ## Tools
            ```python
            {'\n\n'.join(self.tools)}
            ```
            """).strip()
        return system_prompt

    def _get_completion_from_ollama_client(self, messages: list[dict[str, Any]], *, as_json: bool, additional_temperature: float, retires: int = 3) -> str:
        temperature: float = Settings().llm.temperature + additional_temperature
        ollama_messages = [{"role": m["role"], "content": str(m["content"])} for m in messages]
        for _ in range(retires):
            if self.client is None:
                response = ollama.chat(
                    model=Settings().llm.model,
                    messages=ollama_messages,  # type: ignore
                    stream=False,
                    format='json' if as_json or self.tools else '',
                    options={
                        'temperature': temperature
                    }
                )
                content: str = response['message']["content"]  # type: ignore
                
            else:
                curl_command = f'curl -X POST http://localhost:{Settings().remote_port}/api/chat -d \'{{"model": "{Settings().llm.model}", "messages": {json.dumps(ollama_messages)}, "options": {{ "temperature": {temperature} }}, "stream": false }}\''
                stdin, stdout, stderr = self.client.exec_command(curl_command)
                response = stdout.read().decode('UTF-8')
                content = str(json.loads(response)['message']['content'])

            if not self.tools:
                return content
            else:
                try:
                    json_content = lowercase_keys(json.loads(content))
                    json_content['tools'] = [lowercase_keys(t) for t in json_content['tools']]
                    tool_calls: list[dict[str, Any]] = json_content['tools']
                    __ = OllamaToolsCall(tools=tool_calls)
                    return json.dumps(json_content)
                
                except KeyError:
                    self.logger.debug(f"Didn't get `tools` key, assuming {DIRECTLY_ANSWER_TOOL} tool")
                    return json.dumps({"tools": [{"tool": DIRECTLY_ANSWER_TOOL, "parameters": {DIRECTLY_ANSWER_TOOL_RESPONSE: content}}]})

                except Exception as e:
                    error_msg = f"{e.__class__.__name__}: Error while parsing tools call, JSON is malformed or built with incorrect schema. Use the EXACT JSON schema you were provided!"
                    self.logger.warn(f"{error_msg}\n >> Message: {content}\n >> Full error message: {e}", color='red')
                    messages.append({"role": self.user_role, "content": error_msg})
                    additional_temperature += .3
        
        raise RuntimeError(f"{retires} times the Ollama client failed to provide a valid tools call. Please check the logs for more information.")
    
    def _get_completion_message(self, as_json: bool, messages: list[dict[str, Any]], additional_temperature: float) -> dict[str, Any]:
        content = self._get_completion_from_ollama_client(messages, as_json=as_json, additional_temperature=additional_temperature)
        print(f'CONTENT -- {content}')
        if self.tools:
            tool_calls: list[dict[str, Any]] = json.loads(content)['tools']
            if not DIRECTLY_ANSWER_TOOL in [t['tool'] for t in tool_calls]:
                message = {
                    "role": self.assistant_role,
                    "content": content,
                    TOOL_CALLS: tool_calls
                }
            else:
                directly_respond_tool = [t for t in tool_calls if t['tool'] == DIRECTLY_ANSWER_TOOL][0]
                print(f'XXX - {directly_respond_tool}')
                message = {
                    "role": self.assistant_role, 
                    "content": directly_respond_tool['parameters'][DIRECTLY_ANSWER_TOOL_RESPONSE]
                }
        else:
            message = {
                "role": self.assistant_role, 
                "content": content
            }
        return message

    def _run_tool_call(self, tool_call: dict[str, Any], index: int) -> str | None:
        tool_name = tool_call['tool'].replace('`','').strip()
        if tool_name in self.callables:
            arguments: dict[str, Any] = tool_call["parameters"]
            if tool_name == 'query_magazine_archive':
                arguments['archive'] = self.archive
            self.logger.info(f"Running tool {tool_name}: {str(arguments)}", color='yellow')
            try:
                tool_result = self.callables[tool_name](**arguments)
                return f"Document: {index} {tool_result}"
            except Exception as e:
                self.logger.warn(f"{e.__class__.__name__}: Error while running tool {tool_name} with arguments {arguments}", color='red')
                return None
        else:
            self.logger.warn(f"Model requested non-existing tool: {tool_name}, skipping", color='yellow')
            return None
        
    def _handle_tools(self, messages: list[dict[str, Any]], tool_calls: list) -> tuple[list[dict[str, Any]], bool]:
        tools_message = ''
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._run_tool_call, tool_call, i) for i, tool_call in enumerate(tool_calls)]
        for result in [f.result() for f in futures]:
            if result:
                tools_message = f"{tools_message}\n{result}"
        if tools_message:
            messages.append({"role": "user", "content": tools_message.strip()})
        return messages, bool(tools_message)
