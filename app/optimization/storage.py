import json
from pathlib import Path


class OptimizationStorage:
    """Store and load optimization results."""

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
            json.dumps(data, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )

    def load(self):
        if not self.path.exists():
            return None

        return json.loads(
            self.path.read_text(encoding="utf-8")
        )

    def save_history(self, results, path="data/optimization/history.json"):
        """Save all tested optimization configurations."""
        history_path = Path(path)
        history_path.parent.mkdir(parents=True, exist_ok=True)

        data = []
        for result in results:
            data.append({
                "parameters": result.parameters,
                "profit": result.profit,
                "win_rate": result.win_rate,
                "profit_factor": result.profit_factor,
                "drawdown": result.drawdown,
                "score": result.score,
            })

        history_path.write_text(
            json.dumps(data, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )
