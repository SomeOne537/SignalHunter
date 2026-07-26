from dataclasses import dataclass


@dataclass
class RiskAdjustedScore:
    score: float
    profit: float
    profit_factor: float
    drawdown: float
    stability: float


class RiskAdjustedOptimizerScore:
    """Calculate optimization score with risk control."""

    def calculate(self, metrics):
        profit = metrics.get("profit", 0)
        profit_factor = metrics.get("profit_factor", 0)
        drawdown = metrics.get("drawdown", 0)
        stability = metrics.get("stability", 0)

        score = round(
            profit_factor
            + profit / 100
            + stability
            - drawdown / 100,
            3,
        )

        return RiskAdjustedScore(
            score=score,
            profit=profit,
            profit_factor=profit_factor,
            drawdown=drawdown,
            stability=stability,
        )
