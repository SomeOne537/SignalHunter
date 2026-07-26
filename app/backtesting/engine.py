from app.trading.engine import SignalEngine
from .trades import BacktestTrade
from .metrics import calculate_metrics
from .risk import calculate_levels


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
            entry = candles[-1].close
            stop_loss, take_profit = calculate_levels(
                entry,
                signal.direction.value,
            )

            trades.append(
                BacktestTrade(
                    direction=signal.direction.value,
                    entry=entry,
                    exit=entry,
                    stop_loss=stop_loss,
                    take_profit=take_profit,
                    profit=0,
                    result="OPEN",
                )
            )

        return {
            "trades": trades,
            "metrics": calculate_metrics(trades),
        }
