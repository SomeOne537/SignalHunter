from dataclasses import dataclass


@dataclass
class BacktestResult:
    total_signals: int
    correct_signals: int
    accuracy: float


class Backtester:
    """Simple historical signal evaluation engine."""

    def run(self, signals, future_prices, horizon: int = 1):
        correct = 0

        for signal, future in zip(signals, future_prices):
            if signal.direction == "BUY" and future > 0:
                correct += 1
            elif signal.direction == "SELL" and future < 0:
                correct += 1

        total = len(signals)

        return BacktestResult(
            total_signals=total,
            correct_signals=correct,
            accuracy=(correct / total) if total else 0.0,
        )
