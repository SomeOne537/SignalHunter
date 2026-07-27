class SignalValidator:
    """Validate signals before sending them to the user.

    Uses calculated indicators only. Does not access broker accounts
    or execute trades.
    """

    def validate(self, indicators, decision, current_price=None):
        reasons = []

        if decision["direction"] == "NO_TRADE":
            reasons.append("low_score")

        # Trend strength filter
        if indicators.adx is not None and indicators.adx < 20:
            reasons.append("weak_trend")

        # Market activity filter
        if indicators.volatility is not None and indicators.volatility == 0:
            reasons.append("no_volatility")

        # Momentum filters
        if decision["direction"] == "BUY":
            if indicators.rsi is not None and indicators.rsi > 70:
                reasons.append("overbought")
            if indicators.stoch_rsi is not None and indicators.stoch_rsi > 0.8:
                reasons.append("stoch_rsi_overbought")

        if decision["direction"] == "SELL":
            if indicators.rsi is not None and indicators.rsi < 30:
                reasons.append("oversold")
            if indicators.stoch_rsi is not None and indicators.stoch_rsi < 0.2:
                reasons.append("stoch_rsi_oversold")

        # Bollinger sanity check
        if indicators.bollinger_upper is not None and indicators.bollinger_lower is not None:
            if indicators.bollinger_upper <= indicators.bollinger_lower:
                reasons.append("invalid_bollinger_range")

        # Support/resistance distance filter.
        # Applied only when current price is provided by market data layer.
        if current_price is not None:
            threshold = current_price * 0.001

            if indicators.resistance_level is not None and decision["direction"] == "BUY":
                if abs(indicators.resistance_level - current_price) <= threshold:
                    reasons.append("near_resistance")

            if indicators.support_level is not None and decision["direction"] == "SELL":
                if abs(current_price - indicators.support_level) <= threshold:
                    reasons.append("near_support")

        valid = len(reasons) == 0

        return {
            "valid": valid,
            "direction": decision["direction"] if valid else "NO_TRADE",
            "score": decision["score"],
            "reasons": reasons,
        }
