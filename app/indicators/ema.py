def calculate_ema(values: list[float], period: int) -> float:
    """Calculate EMA value for a price series."""
    if not values:
        return 0.0

    multiplier = 2 / (period + 1)
    ema = values[0]

    for price in values[1:]:
        ema = (price - ema) * multiplier + ema

    return ema


def ema_trend(values: list[float]) -> dict:
    return {
        "ema20": calculate_ema(values, 20),
        "ema50": calculate_ema(values, 50),
    }
