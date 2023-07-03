"""
trash
"""

import loguru

from .config import Config


def logger_from_config(config: Config):
    return loguru.logger
