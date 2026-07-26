from dataclasses import dataclass
from datetime import datetime


@dataclass
class Signal:
    """Unified trading signal representation."""

    direction: str
    score: int
    confidence: float
    symbol: str | None = None
    timeframe: str | None = None
    created_at: datetime | None = None
    reason: list[str] | None = None
