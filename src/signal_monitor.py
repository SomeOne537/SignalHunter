"""Signal monitoring utilities for SignalHunter.

Stores generated trading signals and their metadata for later analysis.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Dict, List


@dataclass
class SignalRecord:
    symbol: str
    action: str
    score: float
    indicators: Dict[str, float]
    created_at: str


class SignalMonitor:
    def __init__(self) -> None:
        self.history: List[SignalRecord] = []

    def add_signal(self, symbol: str, action: str, score: float, indicators: Dict[str, float]) -> SignalRecord:
        record = SignalRecord(
            symbol=symbol,
            action=action,
            score=score,
            indicators=indicators,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        self.history.append(record)
        return record

    def get_history(self) -> List[dict]:
        return [asdict(item) for item in self.history]
