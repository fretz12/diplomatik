from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.postgres_syntax_policy import \
    PostgresSyntaxPolicy
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.exceptions.exceptions import DataEngineException


class SyntaxPolicyFactory:
    @staticmethod
    def construct(source_type: DataSourceType) -> SyntaxPolicy:
        connectors = {
            DataSourceType.postgres: PostgresSyntaxPolicy
        }

        if source_type not in connectors:
            raise DataEngineException(f"Unknown data source type: {source_type}")

        return connectors[source_type]()
