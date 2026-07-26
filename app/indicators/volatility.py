def calculate_volatility(values: list[float]) -> float:
    """Simple volatility estimation."""
    if len(values) < 2:
        return 0.0

    changes = [
        abs(current - previous)
        for current, previous in zip(values[1:], values[:-1])
    ]

    return sum(changes) / len(changes)


def is_flat_market(values: list[float], threshold: float = 0.001) -> bool:
    return calculate_volatility(values) < threshold
