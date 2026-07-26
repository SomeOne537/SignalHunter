from statistics import mean


def calculate_volume_strength(candles, period: int = 20) -> float:
    """Estimate current volume strength relative to average volume."""
    volumes = [getattr(candle, "volume", 0) for candle in candles]

    if len(volumes) < period:
        return 0.0

    average = mean(volumes[-period:])
    if average == 0:
        return 0.0

    return volumes[-1] / average
