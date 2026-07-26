from itertools import product

from .parameters import (
    EMA_FAST_VALUES,
    EMA_SLOW_VALUES,
    RSI_PERIOD_VALUES,
    RSI_OVERSOLD_VALUES,
    RSI_OVERBOUGHT_VALUES,
    MACD_VALUES,
    RSI_WEIGHT_VALUES,
    MACD_WEIGHT_VALUES,
    ADX_WEIGHT_VALUES,
    SIGNAL_SCORE_THRESHOLD_VALUES,
    BUY_CONFIRMATION_WEIGHT_VALUES,
    SELL_CONFIRMATION_WEIGHT_VALUES,
    WEAK_SIGNAL_PENALTY_VALUES,
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
        RSI_WEIGHT_VALUES,
        MACD_WEIGHT_VALUES,
        ADX_WEIGHT_VALUES,
        SIGNAL_SCORE_THRESHOLD_VALUES,
        BUY_CONFIRMATION_WEIGHT_VALUES,
        SELL_CONFIRMATION_WEIGHT_VALUES,
        WEAK_SIGNAL_PENALTY_VALUES,
    ):
        yield {
            "ema_fast": values[0],
            "ema_slow": values[1],
            "rsi_period": values[2],
            "rsi_oversold": values[3],
            "rsi_overbought": values[4],
            "macd": values[5],
            "rsi_weight": values[6],
            "macd_weight": values[7],
            "adx_weight": values[8],
            "signal_score_threshold": values[9],
            "buy_confirmation_weight": values[10],
            "sell_confirmation_weight": values[11],
            "weak_signal_penalty": values[12],
        }
