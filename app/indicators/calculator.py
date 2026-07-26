from .ema import ema_trend
from .snapshot import IndicatorSnapshot


class IndicatorCalculator:
    """Calculate technical indicators from candle data."""

    def calculate(self, candles):
        if not candles:
            return IndicatorSnapshot()

        closes = [c.close for c in candles]
        ema_values = ema_trend(closes)

        return IndicatorSnapshot(
            ema_fast=ema_values["ema20"],
            ema_slow=ema_values["ema50"],
            volatility=self._volatility(closes),
        )

    def _volatility(self, values):
        if len(values) < 2:
            return 0.0

        changes = [
            abs(current - previous)
            for current, previous in zip(values[1:], values[:-1])
        ]

        return sum(changes) / len(changes)
