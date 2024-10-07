import logging

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    log_level: int = Field(default=logging.INFO, env="LOG_LEVEL")
    debug: bool = Field(default=False, env="DEBUG")
    interval: int = Field(default=60, env="INTERVAL")

    captcha_user_agent: str = Field(
        default="Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        env="CAPTCHA_USER_AGENT",
    )

    vfs_url: str = Field(
        default="https://online.vfsglobal.com/Global-Appointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/DkngnsuyV06lOAvm8bxUnGJJuvKsIkLE4ykj+VjhbSUR8Hopef3ZGxHhSzt9qb9qQ==",
        env="VFS_URL",
    )
    vfs_email: str = Field(..., env="VFS_EMAIL")
    vfs_password: str = Field(..., env="VFS_PASSWORD")

    vfs_password: str = Field(..., env="VFS_URL")


settings = Settings()
