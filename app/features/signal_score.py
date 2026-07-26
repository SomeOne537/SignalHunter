from dataclasses import dataclass


@dataclass
class SignalScore:
    score: int
    direction: str


def calculate_signal_score(indicators) -> SignalScore:
    """Convert indicator values into a normalized trading score."""
    score = 0

    if indicators.ema_fast is not None and indicators.ema_slow is not None:
        score += 2 if indicators.ema_fast > indicators.ema_slow else -2

    if indicators.rsi is not None:
        if indicators.rsi < 30:
            score += 1
        elif indicators.rsi > 70:
            score -= 1

    if indicators.macd is not None:
        score += 2 if indicators.macd > 0 else -2

    if indicators.adx is not None and indicators.adx > 25:
        score += 1

    if indicators.volume_strength is not None and indicators.volume_strength > 1:
        score += 1

    if score >= 5:
        direction = "BUY"
    elif score <= -5:
        direction = "SELL"
    else:
        direction = "NO_TRADE"

    return SignalScore(score=score, direction=direction)
