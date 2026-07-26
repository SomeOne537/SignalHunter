import time


class SignalScheduler:
    """Run live signal checks on a selected interval."""

    def __init__(self, evaluator, interval_seconds=60):
        self.evaluator = evaluator
        self.interval_seconds = interval_seconds
        self.running = False

    def start(self, market_provider):
        self.running = True

        while self.running:
            candles = market_provider.get_latest()
            self.evaluator.evaluate(candles)
            time.sleep(self.interval_seconds)

    def stop(self):
        self.running = False
