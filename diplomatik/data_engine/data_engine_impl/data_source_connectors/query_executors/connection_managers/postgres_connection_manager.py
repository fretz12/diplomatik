from sqlalchemy import create_engine
from sqlalchemy.engine import Connection, Engine

from settings import get_settings


class PostgresConnectionManager:
    def get_connection(self) -> Connection:
        settings = get_settings()

        user = settings.postgres_default_user
        password = settings.postgres_default_password
        host = settings.postgres_default_host
        port = settings.postgres_default_port
        database = settings.postgres_default_database

        url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

        return create_engine(url).connect()

    def get_engine(self) -> Engine:
        return self.get_connection().engine
