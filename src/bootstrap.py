"""SignalHunter application bootstrap."""

from .config import Settings
from .signal_monitor import SignalMonitor
from .signal_storage import SignalStorage
from .telegram_notifier import TelegramNotifier


def create_application() -> SignalMonitor:
    settings = Settings.from_env()

    storage = SignalStorage(settings.data_path)
    notifier = TelegramNotifier(
        bot_token=settings.telegram_bot_token,
        chat_id=settings.telegram_chat_id,
    )

    return SignalMonitor(
        storage=storage,
        notifier=notifier,
    )
