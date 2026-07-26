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


def calculate_average_move(outcomes):
    """Calculate average price movement after signals."""
    if not outcomes:
        return 0.0

    return sum(o.price_change for o in outcomes) / len(outcomes)


def calculate_direction_stats(outcomes):
    """Calculate BUY and SELL signal statistics separately."""
    buy = [o for o in outcomes if o.direction == "BUY"]
    sell = [o for o in outcomes if o.direction == "SELL"]

    return {
        "buy_total": len(buy),
        "buy_success": sum(1 for o in buy if o.successful),
        "sell_total": len(sell),
        "sell_success": sum(1 for o in sell if o.successful),
    }


def calculate_error_distribution(outcomes):
    """Return successful and failed signal counts."""
    return {
        "successful": sum(1 for o in outcomes if o.successful),
        "failed": sum(1 for o in outcomes if not o.successful),
    }
