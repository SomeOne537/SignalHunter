import httpx

from app.market.models import Candle
from app.market.provider import MarketProvider


class BinanceProvider(MarketProvider):
    """Binance public API market data provider."""

    BASE_URL = "https://api.binance.com/api/v3/klines"

    INTERVALS = {
        "1m": "1m",
        "5m": "5m",
        "15m": "15m",
        "1h": "1h",
        "4h": "4h",
        "1d": "1d",
    }

    def get_candles(
        self,
        pair: str,
        timeframe: str,
        limit: int = 100,
    ) -> list[Candle]:
        params = {
            "symbol": pair.replace("/", "").upper(),
            "interval": self.INTERVALS.get(timeframe, "15m"),
            "limit": limit,
        }

        with httpx.Client(timeout=10) as client:
            response = client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

        return [
            Candle(
                timestamp=item[0],
                open=float(item[1]),
                high=float(item[2]),
                low=float(item[3]),
                close=float(item[4]),
                volume=float(item[5]),
            )
            for item in data
        ]
