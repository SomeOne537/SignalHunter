"""Signal decision engine for SignalHunter.

Converts indicator values into BUY, SELL or NO_TRADE decisions.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class TradingSignal:
    action: str
    score: float
    indicators: Dict[str, float]


class SignalEngine:
    def __init__(self, buy_threshold: float = 60.0, sell_threshold: float = -60.0) -> None:
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    def calculate_score(self, indicators: Dict[str, float]) -> float:
        score = 0.0

        rsi = indicators.get("rsi", 50)
        if rsi < 30:
            score += 40
        elif rsi > 70:
            score -= 40

        if indicators.get("ema", 0) > indicators.get("sma", 0):
            score += 20
        else:
            score -= 20

        return score

    def generate(self, indicators: Dict[str, float]) -> TradingSignal:
        score = self.calculate_score(indicators)

        if score >= self.buy_threshold:
            action = "BUY"
        elif score <= self.sell_threshold:
            action = "SELL"
        else:
            action = "NO_TRADE"

        return TradingSignal(
            action=action,
            score=round(score, 2),
            indicators=indicators,
        )
