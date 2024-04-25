class ViewedURLs:
    _instance = None
    _memory: list[str] = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ViewedURLs, cls).__new__(cls)
        return cls._instance

    def __getitem__(self, i: int) -> str:
        return self._memory[i]
    
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
