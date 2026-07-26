from dataclasses import dataclass


@dataclass
class BacktestTrade:
    direction: str
    entry: float
    exit: float
    profit: float

