class SignalFormatter:
    """Format trading signals for Telegram messages."""

    def format(self, signal):
        reasons = "\n".join(
            f"- {reason}" for reason in signal.reasons
        )

        return (
            "🚨 SignalHunter Alert\n\n"
            f"Pair: {signal.symbol}\n"
            f"Timeframe: {signal.timeframe}\n\n"
            f"Direction: {signal.direction}\n"
            f"Confidence: {signal.confidence}%\n\n"
            f"Reasons:\n{reasons}"
        )
