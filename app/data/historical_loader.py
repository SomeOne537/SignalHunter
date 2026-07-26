from dataclasses import dataclass
from datetime import datetime


@dataclass
class HistoricalCandle:
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0


class HistoricalDataLoader:
    """Load and normalize historical market candles."""

    def from_records(self, records):
        candles = []

        for record in records:
            candles.append(
                HistoricalCandle(
                    timestamp=record["timestamp"],
                    open=record["open"],
                    high=record["high"],
                    low=record["low"],
                    close=record["close"],
                    volume=record.get("volume", 0.0),
                )
            )

        return candles
