import json
from pathlib import Path


class OptimizationStorage:
    """Store and load best optimization results."""

    def __init__(self, path="data/optimization/best_strategy.json"):
        self.path = Path(path)

    def save(self, result):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "parameters": result.parameters,
            "profit": result.profit,
            "win_rate": result.win_rate,
            "profit_factor": result.profit_factor,
            "drawdown": result.drawdown,
            "score": result.score,
        }

        self.path.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8",
        )

    def load(self):
        if not self.path.exists():
            return None

        return json.loads(
            self.path.read_text(encoding="utf-8")
        )
