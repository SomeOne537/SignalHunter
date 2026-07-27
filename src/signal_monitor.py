"""Signal monitoring utilities for SignalHunter.

Stores generated trading signals and automatically persists them.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Dict, List, Optional

from .signal_storage import SignalStorage


@dataclass
class SignalRecord:
    symbol: str
    action: str
    score: float
    indicators: Dict[str, float]
    created_at: str


class SignalMonitor:
    def __init__(self, storage: Optional[SignalStorage] = None) -> None:
        self.storage = storage or SignalStorage()
        self.history: List[SignalRecord] = [
            SignalRecord(**item) for item in self.storage.load()
        ]

    def add_signal(self, symbol: str, action: str, score: float, indicators: Dict[str, float]) -> SignalRecord:
        record = SignalRecord(
            symbol=symbol,
            action=action,
            score=score,
            indicators=indicators,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        self.history.append(record)
        self.storage.save(self.get_history())
        return record

    def get_history(self) -> List[dict]:
        return [asdict(item) for item in self.history]
