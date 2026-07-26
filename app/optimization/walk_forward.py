from dataclasses import dataclass


@dataclass
class WalkForwardResult:
    windows: int
    average_score: float
    stability: float
    passed: bool


class WalkForwardValidator:
    """Validate strategy stability across sequential time windows."""

    def validate(self, windows, max_deviation=0.2):
        if not windows:
            return WalkForwardResult(
                windows=0,
                average_score=0,
                stability=0,
                passed=False,
            )

        scores = [window.get("score", 0) for window in windows]
        average_score = sum(scores) / len(scores)

        if average_score == 0:
            stability = 0
        else:
            deviations = [
                abs(score - average_score) / abs(average_score)
                for score in scores
            ]
            stability = max(0, 1 - sum(deviations) / len(deviations))

        return WalkForwardResult(
            windows=len(windows),
            average_score=round(average_score, 3),
            stability=round(stability, 3),
            passed=stability >= (1 - max_deviation),
        )
