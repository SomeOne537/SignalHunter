from telegram import Update
from telegram.ext import ContextTypes

from .keyboards import pairs_keyboard, timeframe_keyboard
from app.market.factory import get_market_provider
from app.trading.engine import SignalEngine
from app.output.formatter import format_signal


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

    await update.message.reply_text(f"🔎 Анализирую {pair} {timeframe}...")

    provider = get_market_provider()
    candles = provider.get_candles(pair, timeframe)

    engine = SignalEngine()
    trading_signal = engine.generate(
        pair=pair,
        timeframe=timeframe,
        candles=candles,
    )

    await update.message.reply_text(format_signal(trading_signal))
