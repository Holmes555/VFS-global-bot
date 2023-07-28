import logging

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    log_level: int = Field(default=logging.INFO, env='LOG_LEVEL')
    debug: bool = Field(default=False, env='DEBUG')


settings = Settings()
