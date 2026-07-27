def calculate_rsi(values: list[float], period: int = 14) -> float:
    """Calculate RSI from closing prices."""
    if len(values) <= period:
        return 50.0

    gains = []
    losses = []

    for current, previous in zip(values[1:], values[:-1]):
        change = current - previous
        gains.append(max(change, 0))
        losses.append(abs(min(change, 0)))

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)


def calculate_rsi_series(values: list[float], period: int = 14) -> list[float]:
    """Calculate RSI values sequence for secondary indicators."""
    if len(values) <= period:
        return []

    result = []
    for index in range(period, len(values)):
        result.append(calculate_rsi(values[: index + 1], period))

    return result
