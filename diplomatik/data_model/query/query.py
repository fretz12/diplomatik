from abc import ABC
from enum import Enum

from pydantic import BaseModel

from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.query_results.query_result import QueryResultType
from diplomatik.exceptions.exceptions import DataModelException


class QueryType(Enum):
    aggregate = 'aggregate'
    batch = 'batch'
    data_source_management = 'data_source_management'
    delete = 'delete'
    insert = 'insert'
    search = 'search'
    template = 'template'
    union = 'union'
    update = 'update'


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
    data_source_config: DataSourceConfig
    """Config about the data source to query"""

    query_result_config: QueryResultConfig | None = None
    """Config for the query results, if applicable"""

    query_id: str | None = None
    """Optional ID for the query. This is user supplied and up to the user to guarantee its uniqueness. A common way to 
    guarantee uniqueness is to use UUIDs"""

    event_hooks: list[EventHook] | None  = None
    """Event hooks that get executed before or after the query gets executed"""


class Transaction(BaseModel):
    """The list of queries to execute together as a transaction"""
    queries: list[Query]
    """The queries to execute in order"""
