from functools import lru_cache
from typing import Any, cast

from pydantic import BaseSettings, PostgresDsn, validator


class AppSettings(BaseSettings):
    ENV_NAME: str | None = None

    DB_NAME: str | None = None
    DB_USER: str | None = None
    DB_PASS: str | None = None
    DB_HOST: str | None = None
    DB_PORT: str | None = None
    DATABASE_URL: str = ""

    SQL_SHOW_QUERY: bool | None = None

    SECRET_AUTH: str | None = None

    @validator("DATABASE_URL", pre=True)
    def get_database_url(cls, v: str | None, values: dict[str, Any]) -> str:
        if isinstance(v, str) and v:
            return v
        result = cast(
            str,
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                user=values.get("DB_USER"),
                password=values.get("DB_PASS"),
                host=values.get("DB_HOST"),
                port=values.get("DB_PORT"),
                path=f"/{values.get('DB_NAME')}",
            ),
        )
        return result

    class Config:
        env_file = ".env", ".env_local"
        env_file_encoding = "utf-8"


@lru_cache
def get_app_settings() -> AppSettings:
    settings = AppSettings()
    print(f">>> Loading settings for: {settings.ENV_NAME}")
    return settings
