import functools
from time import sleep
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
    

def atomic(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        self._atomic_locks[func.__name__] = self._atomic_locks.get(func.__name__, False)
        while self._atomic_locks[func.__name__]:
            sleep(.5)
        self._atomic_locks[func.__name__] = True
        try:
            output = func(self, *args, **kwargs)
        finally:
            self._atomic_locks[func.__name__] = False
        return output
    return wrapper
