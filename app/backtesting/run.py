import argparse

from app.backtesting.runner import BacktestRunner


class BacktestCLI:
    """Command line interface for running backtests."""

    def run(self, symbol: str, timeframe: str):
        print(f"Starting backtest: {symbol} {timeframe}")

        runner = BacktestRunner()

        # Data provider will be connected in the next stage.
        report = runner.run([])

        print("Backtest finished")
        print(f"Signals: {report.total_signals}")
        print(f"BUY: {report.buy_signals}")
        print(f"SELL: {report.sell_signals}")
        print(f"NO_TRADE: {report.no_trade_signals}")


def main():
    parser = argparse.ArgumentParser(description="Run SignalHunter backtest")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--timeframe", required=True)

    args = parser.parse_args()

    BacktestCLI().run(args.symbol, args.timeframe)


if __name__ == "__main__":
    main()
