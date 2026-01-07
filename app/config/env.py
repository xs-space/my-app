from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = '.env.dev'


class AppSettings(BaseSettings):
    name: str ='app'
    version: str = '0.0.0'

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_prefix='APP_',
        env_file_encoding='utf-8',
        case_sensitive=False,  # 不区分大小写,
        extra='ignore',
        validate_default=True
    )


class MysqlSettings(BaseSettings):
    name: str = '127.0.0.1'
    host: int = 3306
    username: str = 'root'
    password: str = '123456'
    database: str = 'my-app'

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_prefix='MYSQL_',
        env_file_encoding='utf-8',
        case_sensitive=False,  # 不区分大小写,
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
        validate_default=True
    )


settings = Settings()

print(settings.app.name)
