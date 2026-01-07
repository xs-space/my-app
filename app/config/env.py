from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).absolute().parent.parent.parent / '.env.dev'


class AppSettings(BaseSettings):
    name: str
    version: str
    env: str
    debug: bool

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_prefix='APP_',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore',
        validate_default=True
    )


class MysqlSettings(BaseSettings):
    host: str
    port: int
    username: str
    password: str
    database: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_prefix='MYSQL_',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore',
        validate_default=True
    )


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    mysql: MysqlSettings = MysqlSettings()

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding='utf-8',
        case_sensitive=False,  # 不区分大小写,
        extra='ignore',
        validate_default=True  # 验证默认值
    )


settings = Settings()
