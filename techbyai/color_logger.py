import logging
from types import TracebackType
from typing import Mapping, Dict
from ._types import Color

_DEFAULT_LOG_LEVEL = logging.INFO
_DEFAULT_LOGGER_NAME = "techbyai"


class ColorLogger(logging.Logger):
    def __init__(self, name: str, level: int | str) -> None:
        super().__init__(name, level)
        self.propagate = False
        handler = logging.StreamHandler()
        handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.addHandler(handler)

    def _add_color(self, text: str, color: Color) -> str:
        reset = '\033[0m'
        colors: Dict[Color, str] = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m'
        }
        return f'{colors[color]}{text}{reset}'

    def debug(self, msg: object, *args: object, color: Color | None = None, exc_info: bool | tuple[type[BaseException], BaseException, TracebackType | None] | tuple[None, None, None] | BaseException | None = None, stack_info: bool = False, stacklevel: int = 1, extra: Mapping[str, object] | None = None) -> None:
        if color:
            msg = self._add_color(str(msg), color)
        return super().debug(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel, extra=extra)
    
    def info(self, msg: object, *args: object, color: Color | None = None, exc_info: bool | tuple[type[BaseException], BaseException, TracebackType | None] | tuple[None, None, None] | BaseException | None = None, stack_info: bool = False, stacklevel: int = 1, extra: Mapping[str, object] | None = None) -> None:
        if color:
            msg = self._add_color(str(msg), color)
        return super().info(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel, extra=extra)
    
    def warn(self, msg: object, *args: object, color: Color | None = None, exc_info: bool | tuple[type[BaseException], BaseException, TracebackType | None] | tuple[None, None, None] | BaseException | None = None, stack_info: bool = False, stacklevel: int = 1, extra: Mapping[str, object] | None = None) -> None:
        if color:
            msg = self._add_color(str(msg), color)
        return super().warn(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel, extra=extra)
 
    def warning(self, msg: object, *args: object, color: Color | None = None, exc_info: bool | tuple[type[BaseException], BaseException, TracebackType | None] | tuple[None, None, None] | BaseException | None = None, stack_info: bool = False, stacklevel: int = 1, extra: Mapping[str, object] | None = None) -> None:
        if color:
            msg = self._add_color(str(msg), color)
        return super().warning(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel, extra=extra)

    def error(self, msg: object, *args: object, color: Color | None = None, exc_info: bool | tuple[type[BaseException], BaseException, TracebackType | None] | tuple[None, None, None] | BaseException | None = None, stack_info: bool = False, stacklevel: int = 1, extra: Mapping[str, object] | None = None) -> None:
        if color:
            msg = self._add_color(str(msg), color)
        return super().error(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel, extra=extra)
    
    def critical(self, msg: object, *args: object, color: Color | None = None, exc_info: bool | tuple[type[BaseException], BaseException, TracebackType | None] | tuple[None, None, None] | BaseException | None = None, stack_info: bool = False, stacklevel: int = 1, extra: Mapping[str, object] | None = None) -> None:
        if color:
            msg = self._add_color(str(msg), color)
        return super().critical(msg, *args, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel, extra=extra)
    

def get_logger(name: str| None = None, level: str | int | None = None):
    return ColorLogger(name or _DEFAULT_LOGGER_NAME, level=level or _DEFAULT_LOG_LEVEL)
