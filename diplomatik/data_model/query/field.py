from abc import ABC
from enum import Enum

from diplomatik.data_engine.data_engine_api.query_component import QueryComponent
from diplomatik.exceptions.exceptions import DataModelException


class FieldDataType(Enum):
    int32 = 'int32'
    int64 = 'int64'
    float32 = 'float32'
    float64 = 'float64'
    string = 'string'
    date = 'date'

    @classmethod
    def get_by_value(cls, value: str):
        """
        Gets the data type based on its string value

        :param value: the value to match
        :return: the data type
        """
        for type in FieldDataType:
            if type.value == value:
                return type

        raise DataModelException("Invalid field data type")


class Field(QueryComponent, ABC):
    """
    The base class for defining columns, functions, or arbitrary values in a query
    """
    data_type: FieldDataType | None = None
    """The data type for the field"""

    alias: str | None = None
    """Alias for the field"""
