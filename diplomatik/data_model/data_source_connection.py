from abc import ABC, abstractmethod
from enum import Enum

from pydantic import BaseModel

from diplomatik.exceptions.exceptions import DataModelException


@abstractmethod
class DataSourceConnectionInfo(ABC, BaseModel):
    pass


class DatabasePasswordAuthConnectionInfo(DataSourceConnectionInfo):
    host_url: str = ''
    port: int = -1
    username: str = ''
    password: str = ''
    database_name: str = ''

    # def to_cachable_dict(self):
    #     return {
    #         "id": self.id,
    #         "user_id": self.user_id,
    #         "host_url": self.host_url,
    #         "port": self.port,
    #         "username": self.username,
    #         "password": self.password,
    #         "database_name": self.database_name,
    #         "is_enabled": str(self.is_enabled),
    #     }
