from abc import ABC, abstractmethod
from enum import Enum

from pydantic import BaseModel

from diplomatik.data_engine.data_engine_api.data_source_connector import DataSourceConnector
from diplomatik.data_model.query.query_statement import QueryStatement


class QueryComponentType(Enum):
    """The type of query component"""

    column = 'column'
    value = 'value'
    function = 'value'


class QueryComponent(ABC, BaseModel):
    component_type: QueryComponentType

    # @abstractmethod
    # def compile(self, data_source_connector: DataSourceConnector, *args) -> QueryStatement:
    #     """
    #     Converts the query component into a database specific query statement
    #
    #     :param data_source_connector: the data source connector to compile with
    #     :param args: additional args to input
    #     :return: the query statement
    #     """
    #     pass
