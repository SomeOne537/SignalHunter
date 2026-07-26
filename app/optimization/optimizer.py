from .results import OptimizationResult
from .grid import generate_parameter_grid


class StrategyOptimizer:
    """Find best strategy configuration using backtesting."""

    def __init__(self, backtest_engine):
        self.backtest_engine = backtest_engine

    def calculate_score(self, metrics):
        return round(
            metrics.get("profit_factor", 0)
            + metrics.get("win_rate", 0) / 100
            - metrics.get("drawdown", 0) / 100,
            3,
        )

    def evaluate(self, parameters, pair, timeframe, candles):
        result = self.backtest_engine.run(
            pair,
            timeframe,
            candles,
            parameters=parameters,
        )

        metrics = result["metrics"]

        return OptimizationResult(
            parameters=parameters,
            profit=metrics.get("profit", 0),
            win_rate=metrics.get("win_rate", 0),
            profit_factor=metrics.get("profit_factor", 0),
            drawdown=metrics.get("drawdown", 0),
            score=self.calculate_score(metrics),
        )

    def optimize(self, pair, timeframe, candles):
        """Run grid search and return best configuration."""
        results = []

        for parameters in generate_parameter_grid():
            results.append(
                self.evaluate(
                    parameters,
                    pair,
                    timeframe,
                    candles,
                )
            )

        return max(
            results,
            key=lambda result: result.score,
            default=None,
        )
