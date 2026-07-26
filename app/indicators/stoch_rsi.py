def calculate_stoch_rsi(rsi_values: list[float], period: int = 14) -> float:
    """Calculate stochastic RSI value."""
    if len(rsi_values) < period:
        return 0.5

    window = rsi_values[-period:]
    low = min(window)
    high = max(window)

    if high == low:
        return 0.5

    return (window[-1] - low) / (high - low)
