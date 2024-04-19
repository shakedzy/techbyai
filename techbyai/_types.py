from typing import Literal, TypeAlias, Callable, Any


Embedding: TypeAlias = list[float]
ToolsDefType: TypeAlias = dict[Callable, list[tuple[str, dict[str, Any], bool]]]

Color: TypeAlias = Literal[
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan"
]