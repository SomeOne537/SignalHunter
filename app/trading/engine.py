from app.indicators.ema import ema_trend
from app.indicators.rsi import calculate_rsi
from app.indicators.macd import calculate_macd
from app.indicators.volatility import is_flat_market
from app.trading.strategy import analyze_market
from app.trading.scoring import score_signal
from app.trading.risk import is_signal_allowed
from app.market.candles import CandleSeries


class SignalEngine:
    """Connects market data, indicators and trading strategy."""

    def generate(self, pair: str, timeframe: str, candles):
        series = CandleSeries(candles)
        closes = series.closes()

        ema = ema_trend(closes)
        rsi = calculate_rsi(closes)
        macd = calculate_macd(closes)
        flat = is_flat_market(closes)

        signal = analyze_market(
            pair=pair,
            timeframe=timeframe,
            ema20=ema["ema20"],
            ema50=ema["ema50"],
            rsi=rsi,
            macd_positive=macd["bullish"],
            ranging=flat,
        )

        confidence = score_signal(
            30 if ema["ema20"] > ema["ema50"] else 0,
            25 if rsi > 50 else 0,
            25 if macd["bullish"] else 0,
            20 if not flat else 0,
        )

        signal.confidence = confidence

        if not is_signal_allowed(confidence, flat):
            return signal

        return signal
