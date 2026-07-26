from app.trading.engine import SignalEngine
from .trades import BacktestTrade
from .metrics import calculate_metrics
from .simulator import simulate_trade
from .portfolio import Portfolio


class BacktestEngine:
    """Run strategy against historical candles."""

    def __init__(self, signal_engine=None, portfolio=None):
        self.signal_engine = signal_engine or SignalEngine()
        self.portfolio = portfolio or Portfolio()

    def run(self, pair, timeframe, candles):
        trades = []

        signal = self.signal_engine.generate(
            pair=pair,
            timeframe=timeframe,
            candles=candles,
        )

        if signal.direction.value != "NO_TRADE" and candles:
            result = simulate_trade(
                signal.direction.value,
                candles,
            )

            entry, exit_price, status = result
            stop_loss = min(entry, exit_price)
            take_profit = max(entry, exit_price)

            profit = (
                exit_price - entry
                if signal.direction.value == "CALL"
                else entry - exit_price
            )

            trade = BacktestTrade(
                direction=signal.direction.value,
                entry=entry,
                exit=exit_price,
                stop_loss=stop_loss,
                take_profit=take_profit,
                profit=profit,
                result=status,
            )

            trades.append(trade)
            self.portfolio.apply_profit(profit)

        return {
            "trades": trades,
            "metrics": calculate_metrics(trades),
            "portfolio": {
                "balance": self.portfolio.balance,
                "return_percent": self.portfolio.return_percent,
            },
        }
