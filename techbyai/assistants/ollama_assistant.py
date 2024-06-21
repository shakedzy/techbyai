import json
from concurrent.futures import ThreadPoolExecutor
from pydantic import BaseModel, RootModel, ValidationError
from paramiko.client import SSHClient
from typing import Any, Callable, Type
from .base_assistant import BaseAssistant, AssistantResponse
from ..settings import Settings
from ..tools import TOOLS_PARAMS_DEFINITIONS
from ..archive import Archive


class OllamaAssistant(BaseAssistant):
    def __init__(self, definition: str, client: SSHClient | None, *, tools: list[Callable] = [], name: str | None = None, archive: Archive | None = None) -> None:
        super().__init__(definition, name=name, archive=archive)
        self.client = client
        self.tools = self._build_tools(tools) if tools else None

     