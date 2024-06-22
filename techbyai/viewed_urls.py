from .color_logger import get_logger


class ViewedURLs:
    _instance = None
    _memory: list[str] = []
    logger = get_logger()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ViewedURLs, cls).__new__(cls)
        return cls._instance

    def __getitem__(self, i: int) -> str:
        url = self._memory[i]
        self.logger.debug(f'Retrieving URL {i}: {url}')
        return url
    
    def __len__(self) -> int:
        return len(self._memory)
    
    def clear(self) -> None:
        self._memory = []

    def add(self, url: str) -> int:
        if url in self._memory:
            index = self.index(url)
            self.logger.debug(f'Adding URL: {url} [already in memory, index: {index}]')
        else:
            index = len(self) - 1
            self._memory.append(url)
            self.logger.debug(f'Adding URL: {url} [index: {index}]')
        return index
    
    def index(self, url: str) -> int:
        return self._memory.index(url)
    
    def pop(self, i: int) -> str:
        return self._memory.pop(i)
    
    def remove(self, url: str) -> None:
        return self._memory.remove(url)
    
    def get_all(self) -> dict[int, str]:
        return {index: url for index, url in enumerate(self._memory)}
