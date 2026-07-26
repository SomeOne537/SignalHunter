MIN_CONFIDENCE = 70
SIGNAL_COOLDOWN_MINUTES = 15


def is_signal_allowed(confidence: int, market_is_flat: bool) -> bool:
    if confidence < MIN_CONFIDENCE:
        return False
    if market_is_flat:
        return False
    return True
