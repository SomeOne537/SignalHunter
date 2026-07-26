RISK_PER_TRADE = 0.01
STOP_LOSS_PERCENT = 0.01
TAKE_PROFIT_PERCENT = 0.02


def calculate_levels(entry: float, direction: str):
    if direction == "CALL":
        return (
            entry * (1 - STOP_LOSS_PERCENT),
            entry * (1 + TAKE_PROFIT_PERCENT),
        )

    return (
        entry * (1 + STOP_LOSS_PERCENT),
        entry * (1 - TAKE_PROFIT_PERCENT),
    )
