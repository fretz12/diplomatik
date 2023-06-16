from typing import TypeVar

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.insert_query_builders.default_insert_values_query_builder import \
    DefaultInsertValuesQueryBuilder
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.insert_query import InsertQuery, InsertType
from diplomatik.exceptions.exceptions import DataEngineException

T = TypeVar("T", bound=InsertQuery)


class InsertQueryBuilderFactory:
    @staticmethod
    def construct(insert_type: InsertType, source_type: DataSourceType, insert_query: T):
        builders = {
            (InsertType.values, DataSourceType.postgres): DefaultInsertValuesQueryBuilder,
        }

        if (insert_type, source_type) not in builders:
            raise DataEngineException(f"Unsupported insert type: {insert_type}")

        return builders[(insert_type, source_type)](source_type, insert_query)
