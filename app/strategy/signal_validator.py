class SignalValidator:
    """Validate trading signals before sending them to the user."""

    def validate(self, indicators, decision):
        reasons = []

        if decision["direction"] == "NO_TRADE":
            reasons.append("low_score")

        if indicators.adx is not None and indicators.adx < 20:
            reasons.append("weak_trend")

        if indicators.volatility is not None and indicators.volatility == 0:
            reasons.append("no_volatility")

        valid = len(reasons) == 0

        return {
            "valid": valid,
            "direction": decision["direction"] if valid else "NO_TRADE",
            "score": decision["score"],
            "reasons": reasons,
        }
