from .color_logger import get_logger


class ViewedURLs:
    _instance = None
    _memory: list[str] = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ViewedURLs, cls).__new__(cls)
        return cls._instance

    def __getitem__(self, i: int) -> str:
        url = self._memory[i]
        get_logger().debug(f'Retrieving URL {i}: {url}')
        return url
    
    def __len__(self) -> int:
        return len(self._memory)
    
    def clear(self) -> None:
        self._memory = []

    def append(self, url: str) -> int:
        self._memory.append(url)
        return len(self) - 1
    
    def index(self, url: str) -> int:
        return self._memory.index(url)
    
    def pop(self, i: int) -> str:
        return self._memory.pop(i)
    
    def remove(self, url: str) -> None:
        return self._memory.remove(url)
