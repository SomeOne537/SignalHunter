from .risk import calculate_levels


def simulate_trade(direction: str, candles):
    """Simulate a single trade through following candles."""
    if not candles:
        return None

    entry = candles[0].close
    stop_loss, take_profit = calculate_levels(entry, direction)

    for candle in candles[1:]:
        if direction == "CALL":
            if candle.low <= stop_loss:
                return entry, stop_loss, "LOSS"
            if candle.high >= take_profit:
                return entry, take_profit, "WIN"

        if direction == "PUT":
            if candle.high >= stop_loss:
                return entry, stop_loss, "LOSS"
            if candle.low <= take_profit:
                return entry, take_profit, "WIN"

    return entry, candles[-1].close, "CLOSE"
