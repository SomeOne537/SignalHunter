"""M1 candle management for SignalHunter.

Keeps recent market candles and prevents duplicate processing.
"""

from typing import List, Optional

from .market_data import Candle


class CandleManager:
    def __init__(self, max_size: int = 200) -> None:
        self.max_size = max_size
        self._candles: List[Candle] = []
        self._last_timestamp = None

    def add_candle(self, candle: Candle) -> bool:
        """Add a new candle if it has not been processed already."""
        if self._last_timestamp == candle.timestamp:
            return False

        self._candles.append(candle)
        self._last_timestamp = candle.timestamp

        if len(self._candles) > self.max_size:
            self._candles.pop(0)

        return True

    def add_candles(self, candles: List[Candle]) -> int:
        added = 0
        for candle in candles:
            if self.add_candle(candle):
                added += 1
        return added

    def get_candles(self, limit: Optional[int] = None) -> List[Candle]:
        if limit is None:
            return list(self._candles)
        return self._candles[-limit:]
