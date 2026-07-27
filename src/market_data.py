"""Market data interface for SignalHunter.

Provides a common structure for OHLC candle data sources.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Protocol


@dataclass
class Candle:
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


class MarketDataProvider(Protocol):
    def get_candles(self, symbol: str, limit: int = 100) -> List[Candle]:
        """Return OHLC candles for a symbol."""
        ...


class MockMarketDataProvider:
    """Temporary provider for testing pipeline integration."""

    def get_candles(self, symbol: str, limit: int = 100) -> List[Candle]:
        return []
