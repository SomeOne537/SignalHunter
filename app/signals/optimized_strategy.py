from pathlib import Path
import json


class OptimizedStrategyLoader:
    """Load validated optimizer parameters for live signal generation."""

    def __init__(self, path="data/optimization/best_strategy.json"):
        self.path = Path(path)

    def load_parameters(self):
        if not self.path.exists():
            return None

        data = json.loads(
            self.path.read_text(encoding="utf-8")
        )

        return data.get("parameters", data)


class OptimizedSignalEngine:
    """Signal engine wrapper using optimized strategy parameters."""

    def __init__(self, signal_engine, loader=None):
        self.signal_engine = signal_engine
        self.loader = loader or OptimizedStrategyLoader()

    def generate(self, market_data):
        parameters = self.loader.load_parameters()

        return self.signal_engine.generate(
            market_data,
            parameters=parameters,
        )
