def sma(values: list[float], period: int) -> list[float]:
    if len(values) < period:
        return []

    return [
        sum(values[i:i + period]) / period
        for i in range(len(values) - period + 1)
    ]


def ema(values: list[float], period: int) -> list[float]:
    if len(values) < period:
        return []

    multiplier = 2 / (period + 1)
    result = [sum(values[:period]) / period]

    for value in values[period:]:
        result.append(
            (value - result[-1]) * multiplier + result[-1]
        )

    return result
