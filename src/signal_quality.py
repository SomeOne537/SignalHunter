"""Signal quality evaluation for SignalHunter.

Tracks signal outcomes and calculates basic performance metrics.
"""

from collections import defaultdict
from typing import Dict, List


class SignalQualityEvaluator:
    def __init__(self, signals: List[Dict]) -> None:
        self.signals = signals

    def evaluated_count(self) -> int:
        return len([s for s in self.signals if "result" in s])

    def success_rate(self) -> float:
        evaluated = [s for s in self.signals if "result" in s]
        if not evaluated:
            return 0.0

        successful = [s for s in evaluated if s.get("result") == "SUCCESS"]
        return round(len(successful) / len(evaluated) * 100, 2)

    def strategy_performance(self) -> Dict[str, Dict[str, float]]:
        stats = defaultdict(lambda: {"total": 0, "success": 0})

        for signal in self.signals:
            strategy = signal.get("strategy", "UNKNOWN")
            stats[strategy]["total"] += 1
            if signal.get("result") == "SUCCESS":
                stats[strategy]["success"] += 1

        for strategy in stats:
            total = stats[strategy]["total"]
            stats[strategy]["success_rate"] = round(stats[strategy]["success"] / total * 100, 2) if total else 0

        return dict(stats)

    def report(self) -> Dict:
        return {
            "evaluated": self.evaluated_count(),
            "success_rate": self.success_rate(),
            "strategies": self.strategy_performance(),
        }
