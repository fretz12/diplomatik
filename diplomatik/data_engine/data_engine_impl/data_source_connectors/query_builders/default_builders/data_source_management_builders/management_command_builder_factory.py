from typing import TypeVar

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.data_source_management_builders.create_table_builder import \
    CreateTableBuilder
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType
from diplomatik.exceptions.exceptions import DataEngineException

T = TypeVar("T", bound=DataSourceManagementCommand)


class ManagementCommandBuilderFactory:
    @staticmethod
    def construct(command_type: DataSourceManagementCommandType, component_compiler: QueryComponentCompiler,
                  syntax_policy: SyntaxPolicy, command: T):
        builders = {
            DataSourceManagementCommandType.create_table: CreateTableBuilder,
        }

        if command_type not in builders:
            raise DataEngineException(f"Command type {command_type} is not supported")

        return builders[command_type](component_compiler, syntax_policy, command)
