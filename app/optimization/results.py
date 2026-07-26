from dataclasses import dataclass


@dataclass
class OptimizationResult:
    parameters: dict
    profit: float
    win_rate: float
    profit_factor: float
    drawdown: float
    score: float
