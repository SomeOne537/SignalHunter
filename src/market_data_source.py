"""Public market data source interface for SignalHunter.

SignalHunter only consumes market data. It does not access user broker
accounts, balances, positions or trading history.
"""

from abc import ABC, abstractmethod
from typing import Dict, List


TIMEFRAME = "M1"


class MarketDataSource(ABC):
    """Abstract public quote/candle provider."""

    @abstractmethod
    def get_candles(self, symbol: str, limit: int = 100) -> List[Dict]:
        """Return M1 OHLC candles."""
        raise NotImplementedError


class MockMarketDataSource(MarketDataSource):
    """Development provider with no external connection."""

    def get_candles(self, symbol: str, limit: int = 100) -> List[Dict]:
        return []
