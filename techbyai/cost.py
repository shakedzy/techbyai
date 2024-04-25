from .settings import Settings

class Cost:
    _instance = None
    _prices: dict[str, tuple[float, float]] = Settings().costs
    _uses: dict[str, int] = {k: 0 for k in _prices.keys()}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cost, cls).__new__(cls)
        return cls._instance

    def __call__(self, precision: int = 2) -> float:
        report = self.report()
        total = sum([v['cost'] for _,v in report.items()])
        return round(total, precision)

    def add(self, section: str, amount: int) -> None:
        if section not in self._uses.keys():
            raise ValueError(f"No pricing defined for {section}!")
        self._uses[section] += amount

    def report(self) -> dict[str, dict[str, float]]:
        compute_cost = lambda t,u: u * self._prices[t][0] / self._prices[t][1]
        dct = {k: {'usage': v, 'cost': compute_cost(k,v)} for k,v in self._uses.items()}
        return dct
