from .models import Candle


class CandleSeries:
    def __init__(self, candles: list[Candle]):
        self.candles = candles

    def closes(self) -> list[float]:
        return [candle.close for candle in self.candles]

    def latest(self) -> Candle | None:
        return self.candles[-1] if self.candles else None
