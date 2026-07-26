from telegram.ext import Application, CommandHandler

from .handlers import start, signal
from app.config import BOT_TOKEN


def create_bot() -> Application:
    """Create Telegram bot application."""
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signal", signal))

    return application
