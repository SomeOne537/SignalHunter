from dataclasses import dataclass

from app.backtesting.pipeline import BacktestPipeline


@dataclass
class BacktestReport:
    total_signals: int
    buy_signals: int
    sell_signals: int
    no_trade_signals: int


class BacktestRunner:
    """Execute complete historical signal generation pipeline."""

    def __init__(self):
        self.pipeline = BacktestPipeline()

    def run(self, candle_sets):
        signals = []

        for candles in candle_sets:
            signals.append(self.pipeline.process(candles))

        return BacktestReport(
            total_signals=len(signals),
            buy_signals=sum(1 for s in signals if s.direction == "BUY"),
            sell_signals=sum(1 for s in signals if s.direction == "SELL"),
            no_trade_signals=sum(1 for s in signals if s.direction == "NO_TRADE"),
        )
