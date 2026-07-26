from dataclasses import dataclass


@dataclass
class ValidationResult:
    passed: bool
    train_score: float
    test_score: float
    degradation: float


class OptimizerValidator:
    """Validate optimized strategies on unseen data."""

    def validate(self, train_metrics, test_metrics, max_degradation=0.2):
        train_score = train_metrics.get("score", 0)
        test_score = test_metrics.get("score", 0)

        if train_score == 0:
            degradation = 1.0
        else:
            degradation = max(0, (train_score - test_score) / abs(train_score))

        return ValidationResult(
            passed=degradation <= max_degradation,
            train_score=train_score,
            test_score=test_score,
            degradation=round(degradation, 3),
        )
