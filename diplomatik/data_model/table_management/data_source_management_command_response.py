from abc import ABC
from enum import Enum

from pydantic import BaseModel

from diplomatik.exceptions.exceptions import DataModelException


class DataSourceManagementCommandResponseType(Enum):
    """
    The data source management command response types
    """
    list_columns = 'list_columns'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the response type based on its string value

        :param value: the value to match
        :return: the aggregation type
        """
        for type in DataSourceManagementCommandResponseType:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid management response")


class DataSourceManagementCommandResponse(BaseModel, ABC):
    """The response base model for a data source management command"""
    response_type: DataSourceManagementCommandResponseType
    """The response type"""
