from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).absolute().parent.parent.parent / ".env.dev"


class Settings(BaseSettings):
    debug: bool

    # app
    app_name: str
    app_version: str

    # database
    db_type: Literal["mysql", "postgres", "sqlite"]
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    pool_size: int
    max_overflow: int
    pool_timeout: int
    pool_pre_ping: bool
    pool_recycle: int
    pool_use_lifo: bool
    echo: bool
    sqlite_db_path: str

    # redis
    redis_host: str
    redis_port: int
    redis_user: str
    redis_password: str
    redis_db: int

    # jwt
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: int
    jwt_refresh_token_expire_minutes: int

    # big model
    deepseek_api_key: str
    deepseek_api_url: str
    deepseek_models: str
    deepseek_default_model: str

    @computed_field
    @property
    def database_url(self) -> str:
        if self.db_type == "postgres":
            return (
                f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
            )
        elif self.db_type == "mysql":
            return f"mysql+aiomysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        elif self.db_type == "sqlite":
            return f"sqlite+aiosqlite:///{self.sqlite_db_path}"
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")

    @computed_field
    @property
    def engine_options(self) -> dict:
        if self.db_type == "postgres" or self.db_type == "mysql":
            return {
                "pool_size": self.pool_size,
                "max_overflow": self.max_overflow,
                "pool_timeout": self.pool_timeout,
                "pool_recycle": self.pool_recycle,
                "pool_use_lifo": self.pool_use_lifo,
                "echo": self.echo,
            }
        return {"echo": self.echo}

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,  # 不区分大小写,
        extra="ignore",
        validate_default=True,  # 验证默认值
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
