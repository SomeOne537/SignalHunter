from .ema import ema_trend
from .rsi import calculate_rsi, calculate_rsi_series
from .macd import calculate_macd
from .atr import calculate_atr
from .volatility import calculate_volatility
from .adx import calculate_adx
from .bollinger import calculate_bollinger
from .stoch_rsi import calculate_stoch_rsi
from .volume import calculate_volume_strength
from .levels import find_support_resistance
from .snapshot import IndicatorSnapshot


class IndicatorCalculator:
    """Calculate technical indicators from candle data."""

    def calculate(self, candles):
        if not candles:
            return IndicatorSnapshot()

        closes = [c.close for c in candles]
        ema_values = ema_trend(closes)
        macd_value = calculate_macd(closes)
        rsi_value = calculate_rsi(closes)
        rsi_series = calculate_rsi_series(closes)
        bollinger = calculate_bollinger(closes)
        levels = find_support_resistance(closes)

        return IndicatorSnapshot(
            ema_fast=ema_values["ema20"],
            ema_slow=ema_values["ema50"],
            rsi=rsi_value,
            macd=macd_value,
            atr=calculate_atr(candles),
            volatility=calculate_volatility(closes),
            adx=calculate_adx(candles),
            bollinger_upper=bollinger["upper"],
            bollinger_middle=bollinger["middle"],
            bollinger_lower=bollinger["lower"],
            stoch_rsi=calculate_stoch_rsi(rsi_series),
            volume_strength=calculate_volume_strength(candles),
            support_level=levels["support"],
            resistance_level=levels["resistance"],
        )
