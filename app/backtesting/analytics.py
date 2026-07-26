def calculate_drawdown(equity_curve):
    if not equity_curve:
        return 0

    peak = equity_curve[0]
    max_drawdown = 0

    for value in equity_curve:
        peak = max(peak, value)
        drawdown = (peak - value) / peak * 100
        max_drawdown = max(max_drawdown, drawdown)

    return round(max_drawdown, 2)


def calculate_recovery_factor(profit, drawdown):
    if drawdown == 0:
        return 0

    return round(profit / drawdown, 2)
