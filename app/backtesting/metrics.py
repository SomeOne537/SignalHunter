def calculate_metrics(trades):
    """Calculate backtest performance statistics."""
    if not trades:
        return {
            "trades": 0,
            "win_rate": 0,
            "profit": 0,
            "profit_factor": 0,
            "drawdown": 0,
        }

    wins = [trade for trade in trades if trade.profit > 0]
    losses = [abs(trade.profit) for trade in trades if trade.profit < 0]
    profit = sum(trade.profit for trade in trades)

    return {
        "trades": len(trades),
        "win_rate": round(len(wins) / len(trades) * 100, 2),
        "profit": round(profit, 2),
        "profit_factor": round(
            sum(w.profit for w in wins) / sum(losses), 2
        ) if losses else 0,
        "drawdown": 0,
    }
