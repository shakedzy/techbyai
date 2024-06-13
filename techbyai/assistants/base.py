from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable
from ..cost import Cost
from ..archive import Archive
from ..color_logger import get_logger


@dataclass
class AssistantResponse:
    content: str
    json: dict[str, Any]
    conversation: list = field(default_factory=list)


class Assistant:
    def __init__(self, definition: str, *, tools: list[Callable] = [], name: str | None = None, archive: Archive | None = None) -> None:
        self.definition = definition
        self.name = name
        self.callables = {f.__name__: f for f in tools}
        self.logger = get_logger()
        self.cost = Cost()
        self.archive = archive 
   
    @abstractmethod
    def do(self, task: str, *, as_json: bool = False, conversation: list = [], _summarize_conversation: bool = False) -> AssistantResponse:
        raise NotImplementedError()
