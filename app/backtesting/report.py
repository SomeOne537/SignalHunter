from dataclasses import dataclass

from app.backtesting.analytics import (
    calculate_average_move,
    calculate_direction_stats,
    calculate_error_distribution,
)


@dataclass
class BacktestReport:
    total_signals: int
    average_move: float
    direction_stats: dict
    error_distribution: dict


class ReportGenerator:
    """Generate a summary report from backtest outcomes."""

    def generate(self, outcomes):
        return BacktestReport(
            total_signals=len(outcomes),
            average_move=calculate_average_move(outcomes),
            direction_stats=calculate_direction_stats(outcomes),
            error_distribution=calculate_error_distribution(outcomes),
        )
