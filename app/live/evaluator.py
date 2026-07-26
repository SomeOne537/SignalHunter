from dataclasses import dataclass


@dataclass
class LiveSignalEvaluation:
    symbol: str
    timeframe: str
    signal: object
    confidence: float


class LiveEvaluator:
    """Evaluate incoming market updates using signal engine."""

    def __init__(self, signal_engine, risk_manager):
        self.signal_engine = signal_engine
        self.risk_manager = risk_manager

    def evaluate(self, market_data):
        signal = self.signal_engine.generate(market_data)

        if not self.risk_manager.allow(signal):
            return None

        return LiveSignalEvaluation(
            symbol=signal.symbol,
            timeframe=signal.timeframe,
            signal=signal,
            confidence=signal.confidence,
        )
