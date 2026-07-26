from statistics import mean, pstdev


def calculate_bollinger(values: list[float], period: int = 20, deviation: float = 2.0):
    """Calculate Bollinger Bands."""
    if len(values) < period:
        return {"upper": None, "middle": None, "lower": None}

    window = values[-period:]
    middle = mean(window)
    std = pstdev(window)

    return {
        "upper": middle + deviation * std,
        "middle": middle,
        "lower": middle - deviation * std,
    }
