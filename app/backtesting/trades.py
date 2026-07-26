from dataclasses import dataclass


@dataclass
class BacktestTrade:
    direction: str
    entry: float
    exit: float
    stop_loss: float
    take_profit: float
    profit: float
    result: str
