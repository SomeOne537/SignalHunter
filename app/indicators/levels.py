def find_support_resistance(values: list[float], window: int = 20):
    """Find simple local support and resistance levels."""
    if len(values) < window:
        return {"support": None, "resistance": None}

    sample = values[-window:]

    return {
        "support": min(sample),
        "resistance": max(sample),
    }
