from .settings import Settings
from .exceptions import CostException
from .decorators import atomic


class Cost:
    _instance = None
    _atomic_locks: dict[str, bool] = {}
    _prices: dict[str, tuple[float, float]] = Settings().costs
    _uses: dict[str, int] = {k: 0 for k in _prices.keys()}
    _max_cost: float = Settings().editorial.max_cost

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cost, cls).__new__(cls)
        return cls._instance

    def __call__(self, precision: int = 2) -> float:
        report = self.report()
        total = sum([v['cost'] for _,v in report.items()])
        return round(total, precision)

    @atomic
    def add(self, section: str, amount: int = 1) -> None:
        if section not in self._uses.keys():
            raise ValueError(f"No pricing defined for {section}!")
        self._uses[section] += amount
        cost = self()
        if cost > self._max_cost:
            raise CostException(f"Cost exceeded threshold! Current cost: {cost}$ [threshold: {round(self._max_cost, 2)}$]")

    def report(self) -> dict[str, dict[str, float]]:
        compute_cost = lambda t,u: u * self._prices[t][0] / self._prices[t][1]
        dct = {k: {'usage': v, 'cost': compute_cost(k,v)} for k,v in self._uses.items()}
        return dct
