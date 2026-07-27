"""Persistent storage for SignalHunter signal history."""

import json
from pathlib import Path
from typing import List, Dict


class SignalStorage:
    def __init__(self, file_path: str = "data/signals.json") -> None:
        self.file_path = Path(file_path)

    def save(self, signals: List[Dict]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(signals, file, ensure_ascii=False, indent=2)

    def load(self) -> List[Dict]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
