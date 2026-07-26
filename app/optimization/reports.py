from dataclasses import dataclass
from datetime import datetime


@dataclass
class OptimizationReport:
    symbol: str
    timeframe: str
    parameters: dict
    metrics: dict
    created_at: str = datetime.utcnow().isoformat()
