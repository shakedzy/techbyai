from typing import Literal, TypeAlias, Dict, Callable, List, Tuple, Any


ToolsDefType: TypeAlias = Dict[Callable, List[Tuple[str, Dict[str, Any], bool]]]

Color: TypeAlias = Literal[
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan"
]