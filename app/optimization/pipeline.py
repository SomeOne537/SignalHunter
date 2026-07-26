from dataclasses import dataclass


@dataclass
class OptimizationPipelineResult:
    best_strategy: object
    validation: object
    saved: bool


class OptimizationPipeline:
    """Run full SignalHunter optimization workflow."""

    def __init__(
        self,
        optimizer,
        ranking,
        validator,
        storage,
    ):
        self.optimizer = optimizer
        self.ranking = ranking
        self.validator = validator
        self.storage = storage

    def run(self, pair, timeframe, candles):
        optimization_result = self.optimizer.optimize(
            pair,
            timeframe,
            candles,
        )

        ranked = self.ranking.rank(
            optimization_result.results,
        )

        best = ranked[0] if ranked else None

        validation = self.validator.validate(
            optimization_result.train_metrics,
            optimization_result.test_metrics,
        )

        if best and validation.passed:
            self.storage.save(best)
            saved = True
        else:
            saved = False

        return OptimizationPipelineResult(
            best_strategy=best,
            validation=validation,
            saved=saved,
        )
