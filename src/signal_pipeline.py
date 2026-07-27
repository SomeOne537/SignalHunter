"""SignalHunter processing pipeline.

Connects market data, indicators, signal generation and monitoring.
"""

from dataclasses import asdict
from typing import Optional

from .indicator_engine import IndicatorEngine
from .market_data import MarketDataProvider
from .signal_engine import SignalEngine
from .signal_monitor import SignalMonitor


class SignalPipeline:
    def __init__(
        self,
        market_data: MarketDataProvider,
        monitor: SignalMonitor,
        indicator_engine: Optional[IndicatorEngine] = None,
        signal_engine: Optional[SignalEngine] = None,
    ) -> None:
        self.market_data = market_data
        self.monitor = monitor
        self.indicator_engine = indicator_engine or IndicatorEngine()
        self.signal_engine = signal_engine or SignalEngine()

    def process(self, symbol: str):
        candles = self.market_data.get_candles(symbol)

        if not candles:
            return None

        indicators = self.indicator_engine.calculate(candles)
        signal = self.signal_engine.generate(indicators)

        self.monitor.add_signal(
            symbol=symbol,
            action=signal.action,
            score=signal.score,
            indicators=signal.indicators,
        )

        return asdict(signal)
