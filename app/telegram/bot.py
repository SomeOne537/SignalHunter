class TelegramBot:
    """Telegram bot interface."""

    def __init__(self, client):
        self.client = client

    def send_message(self, chat_id, text):
        return self.client.send_message(
            chat_id=chat_id,
            text=text,
        )
