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
        msg = update.channel_post
        if msg:
            logger.info(f"to forward: {msg}")

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
