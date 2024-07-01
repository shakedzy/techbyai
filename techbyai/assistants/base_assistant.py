import json
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass, field
from pydantic import BaseModel, RootModel, ValidationError
from typing import Any, Callable, Type
from ..archive import Archive
from ..color_logger import get_logger
from ..cost import Cost
from ..constants import TOOL_CALLS


@dataclass
class AssistantResponse:
    content: str
    json: dict[str, Any]
    conversation: list = field(default_factory=list)


class BaseAssistant:
    def __init__(self, definition: str, *, tools: list[Callable], name: str | None, archive: Archive | None) -> None:
        self.definition = definition
        self.name = name
        self.callables = {f.__name__: f for f in tools}
        self.logger = get_logger()
        self.cost = Cost()
        self.archive = archive

    @property
    def user_role(self) -> str:
        return 'user'
            
    @property
    def assistant_role(self) -> str:
        return 'assistant'
            
    @property
    def system_role(self) -> str:
        return 'system'
        
    @property
    def tool_role(self) -> str:
        return 'tool'

    def get_system_prompt(self) -> str:
        return f"[Today is {datetime.now().strftime('%d %B, %Y')}{', your name is ' + self.name if self.name else ''}]\n{self.definition}"

    @abstractmethod
    def _build_tools(self, tools: list[Callable]):
        raise NotImplementedError()
    
    def _summarize_conversation(self, conversation: list[dict[str, str]]) -> list[dict[str, str]]:
        MAX_WORDS = 3000
        self.logger.debug("Summarizing conversation...", color='cyan')
        count = 0
        for i, message in enumerate(conversation, start=1):
            content: str = message['content'] or ''
            num_words = len([word for word in content.split(' ') if word.strip()])
            self.logger.debug(f"Message {i} by {message['role']} contains {num_words} words")
            if num_words > MAX_WORDS:
                summarized_response = self.do(f"Summarize the text below to no more than {MAX_WORDS}:\n-----\n{message['content']}")
                count += 1
                message['content'] = summarized_response.content
        self.logger.debug(f"Summarized {count} messages")
        return conversation
    
    def _get_assistant_error_message(self, e: Exception, *, as_json: bool, messages: list[dict[str, str]]) -> AssistantResponse:
        error_message = f'ERROR - {e.__class__.__name__}: {e}'
        raise e  # TODO: REMOVE THIS LINE
        if as_json:
            json_error_message = {"error": error_message}
            error_message = json.dumps(json_error_message)
        else:
            json_error_message = {}
        messages.append({
            "role": self.assistant_role,
            "content": error_message
        })
        return AssistantResponse(content=error_message, json=json_error_message, conversation=messages)
    
    def _get_completion_message(self, as_json: bool, messages: list[dict[str, Any]], additional_temperature: float) -> dict[str, Any]:
        raise NotImplementedError()
    
    def _handle_tools(self, messages: list[dict[str, Any]], tool_calls: list) -> tuple[list[dict[str, Any]], bool]:
        raise NotImplementedError()
    
    @abstractmethod
    def do(self, task: str, *, json_schema: Type[BaseModel] | None = None, conversation: list = []) -> AssistantResponse:
        system_prompt = self.get_system_prompt()
        messages = [
            {"role": self.system_role, "content": system_prompt}
            ] + conversation + [
            {"role": self.user_role, "content": task}
        ]

        final_message = False
        additional_temperature: float = 0.0
        while not final_message:
            try:
                assistant_message = self._get_completion_message(as_json=json_schema is not None, messages=messages, additional_temperature=additional_temperature)
            except Exception as e:
                return self._get_assistant_error_message(e, as_json=json_schema is not None, messages=messages)
            messages.append(assistant_message)
            additional_temperature = 0.0

            if TOOL_CALLS in assistant_message:
                messages, any_tool_success = self._handle_tools(messages, assistant_message["tool_calls"])
                if not any_tool_success:
                    # All tool calls were hallucinations. This is a super rare case.
                    messages.pop()  # remove the last message (this the assistant message, asking for non-existing tools)
                    additional_temperature = .3  # increase temperature momentarily to avoid creating the same message again
                    self.logger.warn("All tool-calls were hallucinations, increasing temperature and retrying", color="red")
            elif json_schema:
                try:
                    content: str = assistant_message['content'] or ''
                    loaded_json: dict = json.loads(content)
                    pydantic_json_model = json_schema(root=loaded_json) if issubclass(json_schema, RootModel) else json_schema(**loaded_json)
                    content_json = pydantic_json_model.model_dump(mode='json')
                    final_message = True
                except ValidationError as e:
                    self.logger.warn(f"Got JSON message with incorrect schema:\n{e.json(indent=2)}", color='red')
                    messages.append({
                        "role": self.user_role,
                        "content": "This JSON message is not formatted as requested! Return a JSON according to the format you were given"
                    })
                except Exception as e:
                    self.logger.warn(f"Error decoding message as JSON - {e.__class__.__name__}: {e}", color='red')
                    messages.append({
                        "role": self.user_role,
                        "content": "The message is not formatted as a valid JSON! Return it as a valid JSON according to the format you were given"
                    })
            else:
                content = assistant_message['content'] or ''
                content_json = {}
                final_message = True
        
        messages.pop(0)  # remove system prompt
        return AssistantResponse(content=content, json=content_json, conversation=messages)
                