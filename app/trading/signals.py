from dataclasses import dataclass
from enum import Enum


class SignalDirection(str, Enum):
    CALL = "CALL"
    PUT = "PUT"
    NO_TRADE = "NO_TRADE"


@dataclass
class TradingSignal:
    pair: str
    timeframe: str
    direction: SignalDirection
    confidence: int
    reasons: list[str]
