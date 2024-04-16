class Cost:
    _instance = None
    _cost = 0.0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cost, cls).__new__(cls)
        return cls._instance

    def __str__(self) -> str:
        return str(self._cost)

    def __call__(self, precision: int = 2) -> float:
        return round(self._cost, precision)
    
    def __add__(self, other: float) -> float:
        return self._cost + other
    
    def __sub__(self, other: float) -> float:
        return self._cost - other
    
    def __iadd__(self, other: float):
        self._cost += other
        return self
    
    def __isub__(self, other: float):
        self._cost -= other
        return self
    
    def reset(self) -> None:
        self._cost = 0.0
