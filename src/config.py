"""Configuration management for SignalHunter."""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Settings:
    telegram_bot_token: Optional[str] = None
    telegram_chat_id: Optional[str] = None
    data_path: str = "data/signals.json"
    default_symbol: str = "EURUSD"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            telegram_bot_token=os.getenv("TELEGRAM_BOT_TOKEN"),
            telegram_chat_id=os.getenv("TELEGRAM_CHAT_ID"),
            data_path=os.getenv("SIGNAL_DATA_PATH", "data/signals.json"),
            default_symbol=os.getenv("DEFAULT_SYMBOL", "EURUSD"),
        )

    def validate(self) -> bool:
        return bool(self.telegram_bot_token and self.telegram_chat_id)
