from abc import ABC
from enum import Enum

from pydantic import BaseModel

from diplomatik.exceptions.exceptions import DataModelException


class QueryResultType(Enum):
    """
    The query result type
    """
    py_list = 'py_list'
    """Returns the results as a python list"""

    py_dict = 'py_dict'
    """Returns the results as a python dict"""

    pandas_dataframe = 'pandas_dataframe'
    """Returns the results as a Pandas dataframe"""

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the query result source type based on its string value

        :param value: the value to match
        :return: the query result type
        """
        for type in QueryResultType:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid query result type")


class QueryResult(BaseModel, ABC):
    """
    The base query result class
    """
    result_type: QueryResultType
    """The type of query result"""

    query_id: str | None = None
    """Optional ID that ties the result to the original query ID. This is user supplied and up to the user to guarantee 
    its uniqueness"""
