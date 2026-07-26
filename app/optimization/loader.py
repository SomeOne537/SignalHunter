from app.trading.config import StrategyConfig


class OptimizationLoader:
    """Load optimized strategy parameters into StrategyConfig."""

    def __init__(self, storage):
        self.storage = storage

    def load_config(self) -> StrategyConfig:
        data = self.storage.load()

        if not data:
            return StrategyConfig()

        parameters = data.get("parameters", {})

        return StrategyConfig(
            ema_fast=parameters.get("ema_fast", 20),
            ema_slow=parameters.get("ema_slow", 50),
            rsi_period=parameters.get("rsi_period", 14),
            rsi_oversold=parameters.get("rsi_oversold", 30),
            rsi_overbought=parameters.get("rsi_overbought", 70),
            macd_fast=parameters.get("macd_fast", 12),
            macd_slow=parameters.get("macd_slow", 26),
            macd_signal=parameters.get("macd_signal", 9),
        )
