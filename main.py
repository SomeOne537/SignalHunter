"""SignalHunter entry point."""

from src.bootstrap import create_application


if __name__ == "__main__":
    monitor = create_application()
    print("SignalHunter started")
