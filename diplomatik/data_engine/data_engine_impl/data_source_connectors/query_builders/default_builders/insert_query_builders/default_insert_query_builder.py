from typing import TypeVar

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.insert_query_builders.insert_query_builder_factory import \
    InsertQueryBuilderFactory
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder import QueryBuilder
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.insert_query import InsertQuery
from diplomatik.data_model.query.query_statement import QueryStatement


T = TypeVar("T", bound=InsertQuery)


class DefaultInsertQueryBuilder(QueryBuilder):
    def __init__(self, source_type: DataSourceType, insert_query: T):
        self.insert_query = insert_query

        self.insert_builder = InsertQueryBuilderFactory.construct(insert_query.insert_type, source_type, insert_query)

    def build(self) -> list[QueryStatement]:
        return [self.insert_builder.build()[0]]
