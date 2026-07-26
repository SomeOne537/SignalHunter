from .provider import MarketProvider


class ExchangeMarketProvider(MarketProvider):
    """Adapter for real exchange market APIs.

    Concrete exchange clients should implement fetch_candles().
    """

    def __init__(self, client):
        self.client = client

    def get_candles(self, pair: str, timeframe: str, limit: int = 100):
        return self.client.fetch_candles(
            pair=pair,
            timeframe=timeframe,
            limit=limit,
        )
