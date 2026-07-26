from itertools import product

from .parameters import (
    EMA_FAST_VALUES,
    EMA_SLOW_VALUES,
    RSI_PERIOD_VALUES,
    RSI_OVERSOLD_VALUES,
    RSI_OVERBOUGHT_VALUES,
    MACD_VALUES,
)


def generate_parameter_grid():
    """Generate all strategy parameter combinations."""
    for values in product(
        EMA_FAST_VALUES,
        EMA_SLOW_VALUES,
        RSI_PERIOD_VALUES,
        RSI_OVERSOLD_VALUES,
        RSI_OVERBOUGHT_VALUES,
        MACD_VALUES,
    ):
        yield {
            "ema_fast": values[0],
            "ema_slow": values[1],
            "rsi_period": values[2],
            "rsi_oversold": values[3],
            "rsi_overbought": values[4],
            "macd": values[5],
        }
