from datetime import datetime

from .candles import Candle
from .data_provider import MarketDataProvider


class MockProvider(MarketDataProvider):

    async def get_candles(
        self,
        pair: str,
        timeframe: str,
        limit: int = 100,
    ) -> list[Candle]:
        candles = []
        price = 1.1000

        for _ in range(limit):
            candles.append(
                Candle(
                    time=datetime.now(),
                    open=price,
                    high=price + 0.001,
                    low=price - 0.001,
                    close=price + 0.0005,
                    volume=1000,
                )
            )
            price += 0.0001

        return candles
