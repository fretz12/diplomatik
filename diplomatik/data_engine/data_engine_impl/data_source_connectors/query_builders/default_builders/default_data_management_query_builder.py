from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.data_source_management_builders.management_command_builder_factory import \
    ManagementCommandBuilderFactory
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder import QueryBuilder
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler_factory import \
    QueryComponentCompilerFactory
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy_factory import \
    SyntaxPolicyFactory
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.data_source_management_query import DataSourceManagementQuery
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommandType


class DefaultDataManagementQueryBuilder(QueryBuilder):
    def __init__(self, source_type: DataSourceType, management_query: DataSourceManagementQuery):
        self.management_query = management_query

        syntax_policy = SyntaxPolicyFactory.construct(source_type)
        component_compiler = QueryComponentCompilerFactory.construct(source_type, syntax_policy)

        command_type = DataSourceManagementCommandType.get_by_value(management_query.command.command_type)

        self.command_builder = ManagementCommandBuilderFactory.construct(
            command_type, component_compiler, syntax_policy, management_query.command)

    def build(self) -> list[QueryStatement]:
        return [self.command_builder.build()]
