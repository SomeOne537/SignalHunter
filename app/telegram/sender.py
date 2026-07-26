class TelegramSender:
    """Send prepared signals to Telegram."""

    def __init__(self, bot, chat_id, min_confidence=70):
        self.bot = bot
        self.chat_id = chat_id
        self.min_confidence = min_confidence

    def send(self, signal, message):
        if signal.direction == "NO_TRADE":
            return False

        if signal.confidence < self.min_confidence:
            return False

        self.bot.send_message(
            chat_id=self.chat_id,
            text=message,
        )

        return True
