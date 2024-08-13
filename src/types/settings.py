from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent.parent

    POSTGRES_PASSWORD: str = Field(default=...)
    POSTGRES_USER: str = Field(default=...)
    POSTGRES_DB: str = Field(default=...)
    POSTGRES_HOST: str = Field(default="database")
    POSTGRES_HOST_AUTH_METHOD: str = Field(default=...)


settings = Settings()
