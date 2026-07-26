from dataclasses import dataclass, field


@dataclass
class Portfolio:
    """Virtual portfolio for backtesting."""

    initial_balance: float = 10000.0
    balance: float = 10000.0
    equity_curve: list[float] = field(default_factory=list)

    def apply_profit(self, profit: float):
        self.balance += profit
        self.equity_curve.append(self.balance)

    @property
    def return_percent(self) -> float:
        return round(
            (self.balance - self.initial_balance)
            / self.initial_balance
            * 100,
            2,
        )
