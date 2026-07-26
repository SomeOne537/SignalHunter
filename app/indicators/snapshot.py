from dataclasses import dataclass


@dataclass
class IndicatorSnapshot:
    """Calculated market indicator values."""

    ema_fast: float | None = None
    ema_slow: float | None = None
    rsi: float | None = None
    macd: float | None = None
    atr: float | None = None
    volatility: float | None = None

    adx: float | None = None
    bollinger_upper: float | None = None
    bollinger_middle: float | None = None
    bollinger_lower: float | None = None
    stoch_rsi: float | None = None

    volume_strength: float | None = None
    support_level: float | None = None
    resistance_level: float | None = None
