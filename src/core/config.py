from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class AppConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}.env",
        env_prefix="CONFIG",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
    )

    app: AppConfig = AppConfig()



settings = Settings()