"""
Main package for copy channel telegram bot
"""

import asyncio

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

from .config import read_config
from .utils import logger_from_config


def forwarder(config, logger):
    async def inner(update: Update, context: ContextTypes.DEFAULT_TYPE):
        channel_id = update.channel_post.chat_id
        logger.debug(
            f"channel_id: {channel_id}, source_channel: {config.source_channel_id}"
        )
        if str(channel_id) != config.source_channel_id:
            return

        if not update.channel_post:
            return

        msg = update.channel_post
        logger.info(f"to forward: {msg}")
        await msg.forward(config.destination_channel_id)

    return inner


def main():
    """
    Entrypoint of the bot
    """

    config = read_config()
    logger = logger_from_config(config)

    app = ApplicationBuilder().token(config.token).build()

    app.add_handler(
        MessageHandler(
            filters=filters.ChatType.CHANNEL, callback=forwarder(config, logger)
        )
    )

    app.run_polling()


if __name__ == "__main__":
    main()
