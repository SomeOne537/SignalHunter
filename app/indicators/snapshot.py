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
