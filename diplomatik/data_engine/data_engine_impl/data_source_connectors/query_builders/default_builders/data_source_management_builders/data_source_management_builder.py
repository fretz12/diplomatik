from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand

T = TypeVar("T", bound=DataSourceManagementCommand)


class DataSourceManagementBuilder(ABC, Generic[T]):
    """The base class for data source management builders"""
    def __init__(self, component_compiler: QueryComponentCompiler, syntax_policy: SyntaxPolicy,
                 management_command: T):
        self.component_compiler = component_compiler
        self.syntax_policy = syntax_policy
        self.management_command = management_command

    @abstractmethod
    def build(self) -> QueryStatement:
        """
        Builds the query statement for the data source management command

        :return: the query statement
        """
        pass
