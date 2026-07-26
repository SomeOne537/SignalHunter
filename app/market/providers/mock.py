from app.market.models import Candle
from app.market.provider import MarketProvider


class MockMarketProvider(MarketProvider):
    """Test provider with generated market data."""

    def get_candles(
        self,
        pair: str,
        timeframe: str,
        limit: int = 100,
    ) -> list[Candle]:
        candles = []
        price = 100.0

        for index in range(limit):
            candles.append(
                Candle(
                    timestamp=index,
                    open=price,
                    high=price + 1,
                    low=price - 1,
                    close=price + 0.5,
                    volume=1000,
                )
            )
            price += 0.5

        return candles
