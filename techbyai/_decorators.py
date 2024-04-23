import functools
from typing import Callable
from .color_logger import get_logger


def tool(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            get_logger().error(f'ERROR [{e.__class__.__name__} in {func.__name__}]: {str(e)}', color='red')
            return f'ERROR: {e}'
    return wrapper
    