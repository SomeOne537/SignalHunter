"""Signal analytics module for SignalHunter."""

from collections import Counter, defaultdict
from typing import Dict, List


class SignalAnalytics:
    def __init__(self, signals: List[Dict]) -> None:
        self.signals = signals

    def total_signals(self) -> int:
        return len(self.signals)

    def actions_summary(self) -> Dict[str, int]:
        return dict(Counter(signal.get("action", "UNKNOWN") for signal in self.signals))

    def average_score(self) -> float:
        if not self.signals:
            return 0.0
        return round(sum(signal.get("score", 0) for signal in self.signals) / len(self.signals), 3)

    def symbols_summary(self) -> Dict[str, int]:
        result = defaultdict(int)
        for signal in self.signals:
            result[signal.get("symbol", "UNKNOWN")] += 1
        return dict(result)

    def report(self) -> Dict:
        return {
            "total": self.total_signals(),
            "actions": self.actions_summary(),
            "average_score": self.average_score(),
            "symbols": self.symbols_summary(),
        }
