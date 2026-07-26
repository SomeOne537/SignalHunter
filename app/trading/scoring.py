def score_signal(
    ema_trend: int,
    rsi_momentum: int,
    macd_confirmation: int,
    volatility: int,
) -> int:
    """Calculate signal confidence from indicator factors."""
    score = sum([ema_trend, rsi_momentum, macd_confirmation, volatility])
    return max(0, min(100, score))


def signal_strength(confidence: int) -> str:
    if confidence < 40:
        return "weak"
    if confidence < 70:
        return "medium"
    if confidence < 85:
        return "good"
    return "strong"
