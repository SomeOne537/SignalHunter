from app.trading.engine import SignalEngine
from .trades import BacktestTrade
from .metrics import calculate_metrics


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
            trades.append(
                BacktestTrade(
                    direction=signal.direction.value,
                    entry=entry,
                    exit=entry,
                    profit=0,
                )
            )

        return {
            "trades": trades,
            "metrics": calculate_metrics(trades),
        }
