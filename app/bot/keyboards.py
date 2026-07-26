from telegram import ReplyKeyboardMarkup


def pairs_keyboard():
    return ReplyKeyboardMarkup(
        [
            ["EUR/USD", "GBP/USD"],
            ["USD/JPY", "AUD/USD"],
        ],
        resize_keyboard=True,
    )


def timeframe_keyboard():
    return ReplyKeyboardMarkup(
        [
            ["M1", "M5"],
            ["M15"],
        ],
        resize_keyboard=True,
    )
