from app.trading.engine import SignalEngine
from .trades import BacktestTrade
from .metrics import calculate_metrics
from .simulator import simulate_trade


class BacktestEngine:
    """Run strategy against historical candles."""

    def __init__(self, signal_engine=None):
        self.signal_engine = signal_engine or SignalEngine()

    def run(self, pair, timeframe, candles):
        trades = []

        signal = self.signal_engine.generate(
            pair=pair,
            timeframe=timeframe,
            candles=candles,
        )

        if signal.direction.value != "NO_TRADE" and candles:
            result = simulate_trade(
                signal.direction.value,
                candles,
            )

            entry, exit_price, status = result
            stop_loss = min(entry, exit_price)
            take_profit = max(entry, exit_price)

            profit = (
                exit_price - entry
                if signal.direction.value == "CALL"
                else entry - exit_price
            )

            trades.append(
                BacktestTrade(
                    direction=signal.direction.value,
                    entry=entry,
                    exit=exit_price,
                    stop_loss=stop_loss,
                    take_profit=take_profit,
                    profit=profit,
                    result=status,
                )
            )

        return {
            "trades": trades,
            "metrics": calculate_metrics(trades),
        }
