from app.market.models import Candle
from app.market.provider import MarketProvider


class BinanceProvider(MarketProvider):
    """Binance market data provider placeholder."""

    def get_candles(
        self,
        pair: str,
        timeframe: str,
        limit: int = 100,
    ) -> list[Candle]:
        """Fetch OHLCV candles from Binance API.

        API integration will be added in the next iteration.
        """
        raise NotImplementedError(
            "Binance API connection is not configured yet"
        )
