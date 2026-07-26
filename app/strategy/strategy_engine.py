from app.features.signal_score import calculate_signal_score


class StrategyEngine:
    """Convert indicator snapshots into trading decisions."""

    def evaluate(self, indicators):
        signal = calculate_signal_score(indicators)

        return {
            "direction": signal.direction,
            "score": signal.score,
            "confidence": abs(signal.score) / 10,
        }
