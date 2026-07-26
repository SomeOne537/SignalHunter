def calculate_metrics(trades):
    """Calculate basic backtest statistics."""
    if not trades:
        return {
            "trades": 0,
            "win_rate": 0,
            "profit": 0,
        }

    wins = [trade for trade in trades if trade.profit > 0]

    return {
        "trades": len(trades),
        "win_rate": round(len(wins) / len(trades) * 100, 2),
        "profit": round(sum(t.profit for t in trades), 2),
    }
