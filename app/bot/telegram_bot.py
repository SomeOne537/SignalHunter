import os

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from .handlers import (
    start,
    signal,
    pair_selected,
    timeframe_selected,
)


PAIR_PATTERN = "EUR/USD|GBP/USD|USD/JPY|AUD/USD"
TIMEFRAME_PATTERN = "M1|M5|M15"


def run_bot():
    token = os.getenv("TELEGRAM_TOKEN")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    app.add_handler(
        MessageHandler(
            filters.Regex(PAIR_PATTERN),
            pair_selected,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex(TIMEFRAME_PATTERN),
            timeframe_selected,
        )
    )

    app.run_polling()
