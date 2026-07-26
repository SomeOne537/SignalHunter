from dataclasses import dataclass


@dataclass
class StrategyConfig:
    """Configurable parameters for trading strategy."""

    ema_fast: int = 20
    ema_slow: int = 50

    rsi_period: int = 14
    rsi_oversold: int = 30
    rsi_overbought: int = 70

    macd_fast: int = 12
    macd_slow: int = 26
    macd_signal: int = 9
