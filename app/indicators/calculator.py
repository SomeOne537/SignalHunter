from .snapshot import IndicatorSnapshot


class IndicatorCalculator:
    """Base calculator for technical indicators."""

    def calculate(self, candles):
        if not candles:
            return IndicatorSnapshot()

        closes = [c.close for c in candles]
        last_close = closes[-1]

        return IndicatorSnapshot(
            ema_fast=last_close,
            ema_slow=last_close,
            volatility=0.0,
        )
