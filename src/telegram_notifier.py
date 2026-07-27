"""Telegram notification layer for SignalHunter."""

from typing import Dict, Optional


class TelegramNotifier:
    def __init__(self, bot_token: Optional[str] = None, chat_id: Optional[str] = None) -> None:
        self.bot_token = bot_token
        self.chat_id = chat_id

    def format_signal_message(self, signal: Dict) -> str:
        symbol = signal.get("symbol", "UNKNOWN")
        action = signal.get("action", "NO_TRADE")
        score = signal.get("score", 0)
        indicators = signal.get("indicators", {})

        lines = [
            "SignalHunter Alert",
            f"Symbol: {symbol}",
            f"Action: {action}",
            f"Score: {score}",
        ]

        if indicators:
            lines.append("Indicators:")
            for name, value in indicators.items():
                lines.append(f"- {name}: {value}")

        return "\n".join(lines)

    def send_signal(self, signal: Dict) -> str:
        """Prepare message payload.

        Actual Telegram API transport will be connected in the next stage.
        """
        return self.format_signal_message(signal)
