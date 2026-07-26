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
    stability: float


class OptimizerRanking:
    """Rank optimization results using risk-adjusted quality."""

    def __init__(self, scorer=None):
        self.scorer = scorer

    def rank(self, results, limit=10):
        ranked_results = []

        for result in results:
            if self.scorer:
                metrics = {
                    "profit": result.profit,
                    "profit_factor": result.profit_factor,
                    "drawdown": result.drawdown,
                    "stability": getattr(result, "stability", 0),
                }
                score_result = self.scorer.calculate(metrics)
                score = score_result.score
            else:
                score = result.score

            ranked_results.append((result, score))

        ranked_results.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        ranked = []

        for index, (result, score) in enumerate(ranked_results[:limit], start=1):
            ranked.append(
                RankedStrategy(
                    rank=index,
                    parameters=result.parameters,
                    score=score,
                    profit=result.profit,
                    win_rate=result.win_rate,
                    profit_factor=result.profit_factor,
                    drawdown=result.drawdown,
                    stability=getattr(result, "stability", 0),
                )
            )

        return ranked
