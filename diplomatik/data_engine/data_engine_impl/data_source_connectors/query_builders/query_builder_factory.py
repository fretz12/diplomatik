from typing import TypeVar

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.default_search_query_builder import \
    DefaultSearchQueryBuilder
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder import QueryBuilder
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.query import QueryType, Query

T = TypeVar("T", bound=Query)


class QueryBuilderFactory:
    """
    Factory for creating query builders
    """
    @staticmethod
    def construct(query_type: QueryType, source_type: DataSourceType, query: T) -> QueryBuilder:
        """
        Fetches the query builder based on the query type and source type

        :param query_type: the query type to match
        :param source_type: the query source to match
        :param query: the query to build a statement for
        :return: the query builder
        """
        builders = {
            (QueryType.search, DataSourceType.postgres): DefaultSearchQueryBuilder,
        }

        return builders[(query_type, source_type)](source_type, query)
