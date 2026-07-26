from abc import ABC, abstractmethod

from .candles import Candle


class MarketDataProvider(ABC):

    @abstractmethod
    async def get_candles(
        self,
        pair: str,
        timeframe: str,
        limit: int = 100,
    ) -> list[Candle]:
        pass
