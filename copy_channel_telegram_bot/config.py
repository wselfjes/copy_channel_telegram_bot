"""
Config structure
"""
from pydantic import BaseSettings, Field


class Config(BaseSettings):
    token: str = Field(..., env="telegram_bot_token")
    source_channel_id: str = Field(..., env="source_channel_id")
    destination_channel_id: str = Field(..., env="destination_channel_id")


def read_config() -> Config:
    """
    Read configuration and return Config object
    """
    return Config()
