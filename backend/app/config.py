from functools import lru_cache
import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: str
    API_STR: str = "http://localhost:9091"
    # postgresql
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    POSTGRES_URL: str

    # redis
    REDIS_PASS: str
    REDIS_PORT: int
    REDIS_ARGS: str
    REDIS_URL: str

    # DIFY
    DIFY_URL: str = "https://api.dify.ai/v1"
    DIFY_CHAT_APP_TOKEN: str

    # wechat
    WX_OFFICE_ACCOUNT_TOKEN: str
    WX_DECRYPT_KEY: str
    WX_APPID: str

    # auth
    ACCESS_SECRET_KEY: str
    REFRESH_SECRET_KEY: str
    REDIS_ACCESS_TOKEN_STR: str = "__access_token"
    REDIS_REFRESH_TOKEN_STR: str = "__refresh_token"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 180


class DevSettings(Settings):
    model_config = SettingsConfigDict(env_file=".env.dev")


class PRODSettings(Settings):
    model_config = SettingsConfigDict(env_file=".env.prod")


@lru_cache
def get_settings() -> Settings:
    if os.getenv("ENV", "DEV").upper() == "PROD":
        return PRODSettings()
    else:
        return DevSettings()


settings = get_settings()
