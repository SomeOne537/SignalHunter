from dataclasses import dataclass


@dataclass
class RankedStrategy:
    rank: int
    parameters: dict
    score: float
    profit: float
    win_rate: float
    profit_factor: float
    drawdown: float


class OptimizerRanking:
    """Rank optimization results by quality score."""

    def rank(self, results, limit=10):
        sorted_results = sorted(
            results,
            key=lambda result: result.score,
            reverse=True,
        )

        ranked = []

        for index, result in enumerate(sorted_results[:limit], start=1):
            ranked.append(
                RankedStrategy(
                    rank=index,
                    parameters=result.parameters,
                    score=result.score,
                    profit=result.profit,
                    win_rate=result.win_rate,
                    profit_factor=result.profit_factor,
                    drawdown=result.drawdown,
                )
            )

        return ranked
