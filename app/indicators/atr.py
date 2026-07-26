def calculate_atr(candles, period: int = 14) -> float:
    """Calculate average true range from candles."""
    if len(candles) < 2:
        return 0.0

    ranges = []
    for current, previous in zip(candles[1:], candles[:-1]):
        true_range = max(
            current.high - current.low,
            abs(current.high - previous.close),
            abs(current.low - previous.close),
        )
        ranges.append(true_range)

    values = ranges[-period:]
    return sum(values) / len(values) if values else 0.0
