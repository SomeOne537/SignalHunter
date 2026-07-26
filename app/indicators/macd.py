def calculate_macd(values: list[float]) -> dict:
    """Basic MACD calculation."""
    ema12 = _ema(values, 12)
    ema26 = _ema(values, 26)
    macd = ema12 - ema26

    return {
        "macd": macd,
        "bullish": macd > 0,
    }


def _ema(values: list[float], period: int) -> float:
    if not values:
        return 0.0

    multiplier = 2 / (period + 1)
    result = values[0]

    for value in values[1:]:
        result = (value - result) * multiplier + result

    return result
