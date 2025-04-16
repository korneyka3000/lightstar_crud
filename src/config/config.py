__all__ = ("settings",)

from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


load_dotenv(".env")


class Settings(BaseSettings):
    DB_URL: PostgresDsn


settings = Settings()  # type: ignore[call-arg]
