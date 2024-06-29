from .color_logger import get_logger
from .decorators import atomic


class ViewedURLs:
    _instance = None
    _atomic_locks: dict[str, bool] = {}
    _memory: list[str] = []
    _titles: dict[str, str] = {}
    logger = get_logger()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ViewedURLs, cls).__new__(cls)
        return cls._instance

    def __getitem__(self, i: int) -> str:
        url = self._memory[i]
        return url
    
    def __len__(self) -> int:
        return len(self._memory)
    
    def clear(self) -> None:
        self._memory = []

    @atomic
    def add(self, url: str, *, title: str) -> int:
        if url in self._memory:
            index = self.index(url)
            self.logger.debug(f'Adding URL: {url} [already in memory, index: {index}]')
        else:
            index = len(self) - 1
            self._memory.append(url)
            self._titles[url] = title
            self.logger.debug(f'Adding URL: {url} [index: {index}]')
        return index
    
    def get_title(self, url: str) -> str:
        return self._titles[url]
    
    def index(self, url: str) -> int:
        return self._memory.index(url)
    
    def pop(self, i: int) -> str:
        return self._memory.pop(i)
    
    def remove(self, url: str) -> None:
        return self._memory.remove(url)
    
    def get_all(self) -> dict[int, str]:
        return {index: url for index, url in enumerate(self._memory)}
