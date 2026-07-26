from app.strategy.strategy_engine import StrategyEngine
from app.strategy.signal_validator import SignalValidator
from app.indicators.calculator import IndicatorCalculator
from app.models.signal import Signal


class BacktestPipeline:
    """Run historical candles through the complete signal pipeline."""

    def __init__(self):
        self.indicators = IndicatorCalculator()
        self.strategy = StrategyEngine()
        self.validator = SignalValidator()

    def process(self, candles):
        snapshot = self.indicators.calculate(candles)
        decision = self.strategy.evaluate(snapshot)
        validated = self.validator.validate(snapshot, decision)

        return Signal(
            direction=validated["direction"],
            score=validated["score"],
            confidence=abs(validated["score"]) / 10,
            symbol=None,
            timeframe=None,
            reason=validated["reasons"],
        )
