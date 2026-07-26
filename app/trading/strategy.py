from .signals import SignalDirection, TradingSignal


def analyze_market(
    pair: str,
    timeframe: str,
    ema20: float,
    ema50: float,
    rsi: float,
    macd_positive: bool,
    ranging: bool,
) -> TradingSignal:
    reasons = []

    if not ranging and ema20 > ema50 and rsi > 50 and macd_positive:
        reasons.extend([
            "EMA20 above EMA50",
            "RSI bullish momentum",
            "MACD confirmation",
        ])
        return TradingSignal(pair, timeframe, SignalDirection.CALL, 80, reasons)

    if not ranging and ema20 < ema50 and rsi < 50 and not macd_positive:
        reasons.extend([
            "EMA20 below EMA50",
            "RSI weakness",
            "MACD bearish confirmation",
        ])
        return TradingSignal(pair, timeframe, SignalDirection.PUT, 80, reasons)

    return TradingSignal(
        pair, timeframe, SignalDirection.NO_TRADE, 0, ["Conditions not met"]
    )
