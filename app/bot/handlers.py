from telegram import Update
from telegram.ext import ContextTypes

from .keyboards import pairs_keyboard, timeframe_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Добро пожаловать в SignalHunter\n\n"
        "Ваш Forex-анализатор сигналов.\n\n"
        "/signal — получить сигнал\n"
        "/help — помощь"
    )


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Выберите валютную пару:",
        reply_markup=pairs_keyboard(),
    )


async def pair_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["pair"] = update.message.text
    await update.message.reply_text(
        "Выберите таймфрейм:",
        reply_markup=timeframe_keyboard(),
    )


async def timeframe_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pair = context.user_data.get("pair", "не выбрана")
    timeframe = update.message.text

    await update.message.reply_text(
        f"🔎 Анализирую {pair} {timeframe}...\n\n"
        "Signal Engine будет подключен следующим модулем."
    )
