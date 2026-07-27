"""Technical indicator engine for SignalHunter."""

from typing import Dict, List

from .market_data import Candle


class IndicatorEngine:
    """Calculates technical indicators from OHLC candles."""

    def calculate_ema(self, values: List[float], period: int = 14) -> float:
        if not values:
            return 0.0

        multiplier = 2 / (period + 1)
        ema = values[0]

        for value in values[1:]:
            ema = (value - ema) * multiplier + ema

        return round(ema, 6)

    def calculate_sma(self, values: List[float], period: int = 14) -> float:
        if not values:
            return 0.0

        window = values[-period:]
        return round(sum(window) / len(window), 6)

    def calculate_rsi(self, values: List[float], period: int = 14) -> float:
        if len(values) <= period:
            return 0.0

        gains = []
        losses = []

        for i in range(1, len(values)):
            change = values[i] - values[i - 1]
            gains.append(max(change, 0))
            losses.append(abs(min(change, 0)))

        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period

        if avg_loss == 0:
            return 100.0

        rs = avg_gain / avg_loss
        return round(100 - (100 / (1 + rs)), 3)

    def calculate(self, candles: List[Candle]) -> Dict[str, float]:
        closes = [c.close for c in candles]

        return {
            "sma": self.calculate_sma(closes),
            "ema": self.calculate_ema(closes),
            "rsi": self.calculate_rsi(closes),
        }
