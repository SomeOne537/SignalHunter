from .models import Candle


class MarketProvider:
    """Base market data provider interface."""

    def get_candles(
        self,
        pair: str,
        timeframe: str,
        limit: int = 100,
    ) -> list[Candle]:
        raise NotImplementedError


class MockMarketProvider(MarketProvider):
    def get_candles(
        self,
        pair: str,
        timeframe: str,
        limit: int = 100,
    ) -> list[Candle]:
        return []
