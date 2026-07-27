"""Broker client interface for SignalHunter.

Defines a common abstraction for connecting broker APIs without coupling
trading logic to a specific provider.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List


class BrokerClient(ABC):
    """Abstract broker API client."""

    @abstractmethod
    def get_candles(self, symbol: str, limit: int = 100) -> List[Dict]:
        """Return raw OHLC candle data."""
        raise NotImplementedError

    @abstractmethod
    def get_account_info(self) -> Dict:
        """Return account information."""
        raise NotImplementedError

    @abstractmethod
    def is_connected(self) -> bool:
        """Return connection state."""
        raise NotImplementedError


class MockBrokerClient(BrokerClient):
    """Testing broker implementation."""

    def get_candles(self, symbol: str, limit: int = 100) -> List[Dict]:
        return []

    def get_account_info(self) -> Dict:
        return {"balance": 0, "currency": "USD"}

    def is_connected(self) -> bool:
        return False
