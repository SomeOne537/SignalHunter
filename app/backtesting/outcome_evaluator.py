from dataclasses import dataclass


@dataclass
class TradeOutcome:
    direction: str
    price_change: float
    successful: bool
    horizon: int


class OutcomeEvaluator:
    """Evaluate whether generated signals matched future price movement."""

    def evaluate(self, signal, current_price: float, future_price: float, horizon: int = 1):
        price_change = future_price - current_price

        if signal.direction == "BUY":
            successful = price_change > 0
        elif signal.direction == "SELL":
            successful = price_change < 0
        else:
            successful = False

        return TradeOutcome(
            direction=signal.direction,
            price_change=price_change,
            successful=successful,
            horizon=horizon,
        )
