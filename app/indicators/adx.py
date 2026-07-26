def calculate_adx(candles, period: int = 14) -> float:
    """Simplified ADX strength estimation."""
    if len(candles) <= period:
        return 0.0

    moves = []
    for current, previous in zip(candles[1:], candles[:-1]):
        moves.append(abs(current.close - previous.close))

    avg_move = sum(moves[-period:]) / period
    avg_range = sum(c.high - c.low for c in candles[-period:]) / period

    if avg_range == 0:
        return 0.0

    return min(100.0, (avg_move / avg_range) * 100)
