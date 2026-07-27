"""Signal monitoring utilities for SignalHunter.

Stores generated trading signals, persists them and can notify users.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Dict, List, Optional

from .signal_storage import SignalStorage
from .telegram_notifier import TelegramNotifier


@dataclass
class SignalRecord:
    symbol: str
    action: str
    score: float
    indicators: Dict[str, float]
    created_at: str


class SignalMonitor:
    def __init__(
        self,
        storage: Optional[SignalStorage] = None,
        notifier: Optional[TelegramNotifier] = None,
    ) -> None:
        self.storage = storage or SignalStorage()
        self.notifier = notifier
        self.history: List[SignalRecord] = [
            SignalRecord(**item) for item in self.storage.load()
        ]

    def add_signal(
        self,
        symbol: str,
        action: str,
        score: float,
        indicators: Dict[str, float],
    ) -> SignalRecord:
        record = SignalRecord(
            symbol=symbol,
            action=action,
            score=score,
            indicators=indicators,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

        self.history.append(record)
        self.storage.save(self.get_history())

        if self.notifier:
            self.notifier.send_signal(asdict(record))

        return record

    def get_history(self) -> List[dict]:
        return [asdict(item) for item in self.history]
