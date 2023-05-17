"""
Main package for copy channel telegram bot
"""

import telegram

from .config import read_config


def main():
    """
    Entrypoint of the bot
    """

    config = read_config()

    bot = telegram.Bot(token=config.token)

    # Get the updates from the source channel
    for update in bot.get_updates(chat_id=config.source_channel_id):
        # Get the message from the update
        message = update.message

        # Check if the message is not None and is not a forwarded message
        if message is not None and message.forward_from is None:
            # Send the message to the destination channel
            bot.send_message(chat_id=config.destination_channel_id, text=message.text)


if __name__ == "__main__":
    main()
