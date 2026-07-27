"""Forex market data adapter for SignalHunter.

Provides a placeholder adapter compatible with MarketDataProvider.
A broker/API implementation can be added without changing the pipeline.
"""

from datetime import datetime
from typing import List

from .market_data import Candle


class ForexDataAdapter:
    """Base Forex data adapter.

    Intended to be extended with MetaTrader, OANDA or another broker API.
    """

    def __init__(self, client=None) -> None:
        self.client = client

    def get_candles(self, symbol: str, limit: int = 100) -> List[Candle]:
        if self.client is None:
            return []

        raw_candles = self.client.get_candles(symbol, limit)

        return [
            Candle(
                symbol=symbol,
                timestamp=item["timestamp"] if isinstance(item["timestamp"], datetime) else datetime.fromisoformat(item["timestamp"]),
                open=item["open"],
                high=item["high"],
                low=item["low"],
                close=item["close"],
                volume=item.get("volume", 0),
            )
            for item in raw_candles
        ]
