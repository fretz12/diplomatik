from abc import ABC
from enum import Enum

from pydantic import BaseModel

from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.exceptions.exceptions import DataModelException


class DataSourceType(Enum):
    postgres = 'postgres'

    @classmethod
    def get_by_value(cls, value: str):
        """
        Gets the data source type based on its string value

        :param value: the value to match
        :return: the data source type
        """
        for source in DataSourceType:
            if source.value == value:
                return source

        raise DataModelException(f"{value} is not a valid data source type")


class QueryResultType(Enum):
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


class QueryType(Enum):
    search = 'search'
    aggregate = 'aggregate'
    insert = 'insert'
    delete = 'delete'
    update = 'update'
    rollup = 'rollup'
    data_source_management = 'data_source_management'
    batch = 'batch'
    union = 'union'
    template = 'template'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the query type based on its string value

        :param value: the value to match
        :return: the query type
        """
        for query in QueryType:
            if query.value == value:
                return query

        raise DataModelException(f"{value} is not a valid query type")


class DataSourceConfig(BaseModel):
    """
    The config specifying the targeted data source and its settings
    """
    source_type: DataSourceType
    """The data source type"""


class QueryResultConfig(BaseModel):
    """
    The config specifying the query result and its settings
    """
    result_type: QueryResultType
    """The result type to use"""


class Query(BaseModel, ABC):
    """
    The base query class
    """
    query_type: QueryType
    """The type of query"""

    data_source_config: DataSourceConfig
    """Config about the data source to query"""

    query_result_config: QueryResultConfig | None = None
    """Config for the query results, if applicable"""

    query_id: str | None = None
    """Optional ID for the query. This is user supplied and up to the user to guarantee its uniqueness. A common way to 
    guarantee uniqueness is to use UUIDs"""

    event_hooks: [EventHook] = None
    """Event hooks that get executed before or after the query gets executed"""


class Transaction(BaseModel):
    """The list of queries to execute together as a transaction"""
    queries: [Query]
    """The queries to execute in order"""
