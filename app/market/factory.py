from app.config import MARKET_PROVIDER
from app.market.provider import MarketProvider
from app.market.providers.mock import MockMarketProvider
from app.market.providers.binance import BinanceProvider


def get_market_provider() -> MarketProvider:
    """Create market data provider from configuration."""
    if MARKET_PROVIDER.lower() == "binance":
        return BinanceProvider()

    return MockMarketProvider()
