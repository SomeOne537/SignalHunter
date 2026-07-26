from .ema import ema_trend
from .rsi import calculate_rsi
from .macd import calculate_macd
from .atr import calculate_atr
from .volatility import calculate_volatility
from .snapshot import IndicatorSnapshot


class IndicatorCalculator:
    """Calculate technical indicators from candle data."""

    def calculate(self, candles):
        if not candles:
            return IndicatorSnapshot()

        closes = [c.close for c in candles]
        ema_values = ema_trend(closes)
        macd_values = calculate_macd(closes)

        return IndicatorSnapshot(
            ema_fast=ema_values["ema20"],
            ema_slow=ema_values["ema50"],
            rsi=calculate_rsi(closes),
            macd=macd_values["macd"],
            atr=calculate_atr(candles),
            volatility=calculate_volatility(closes),
        )
