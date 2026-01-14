from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).absolute().parent.parent.parent / ".env.dev"


class Settings(BaseSettings):
    debug: bool

    # app
    app_name: str
    app_version: str
    app_description: str

    # database
    db_type: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

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
    api_key: str
    model_api_url: str
    models_available: str
    default_model: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,  # 不区分大小写,
        extra="ignore",
        validate_default=True,  # 验证默认值
    )


settings = Settings()
