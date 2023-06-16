from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    The global settings that are read from the .env file in the root directory
    """
    postgres_default_user: str = None
    postgres_default_password: str = None
    postgres_default_host: str = None
    postgres_default_port: str = None
    postgres_default_database: str = None

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
