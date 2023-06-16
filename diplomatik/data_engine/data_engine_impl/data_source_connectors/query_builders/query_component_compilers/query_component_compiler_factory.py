from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.default_query_component_compiler import \
    DefaultQueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.exceptions.exceptions import DataEngineException


class QueryComponentCompilerFactory:
    """
    Factory for creating query component compilers
    """
    @staticmethod
    def construct(source_type: DataSourceType, syntax_policy: SyntaxPolicy) -> QueryComponentCompiler:
        """
        Creates a query component compiler

        :param source_type: the source type to match
        :param syntax_policy: the syntax policy to use
        :return: the query component compiler
        """
        builders = {
            DataSourceType.postgres: DefaultQueryComponentCompiler
        }

        if source_type not in builders:
            raise DataEngineException(f"Unsupported data source type: {source_type}")

        return builders[source_type](source_type, syntax_policy)
