from app.trading.signals import TradingSignal


def format_signal(signal: TradingSignal) -> str:
    """Format trading signal for external clients like Telegram."""

    reasons = "\n".join(
        f"• {reason}" for reason in signal.reasons
    )

    return (
        f"SignalHunter 📡\n"
        f"Pair: {signal.pair}\n"
        f"Timeframe: {signal.timeframe}\n"
        f"Direction: {signal.direction.value}\n"
        f"Confidence: {signal.confidence}%\n\n"
        f"Reasons:\n{reasons}"
    )
