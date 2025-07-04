from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class DBConfig(BaseModel):
    url: PostgresDsn

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    auth: str = "/auth"

    @property
    def bearer_token_url(self) -> str:
        parts = (self.prefix, self.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")


class AccessToken(BaseModel):
    lt_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="CONFIG__",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
    )

    app: AppConfig = AppConfig()
    db: DBConfig
    access_token: AccessToken
    api: ApiPrefix = ApiPrefix()


settings = Settings()
