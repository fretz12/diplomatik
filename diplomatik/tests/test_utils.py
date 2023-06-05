import re

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder_factory import \
    QueryBuilderFactory
from diplomatik.data_model.query.query import Query, QueryType
from diplomatik.data_model.query.query_statement import QueryParam

MERGE_WHITESPACES_PATTERN = re.compile(r"\s+")

def merge_whitespaces(target: str) -> str:
    """
    Removes all leading and trailing whitespaces from a string. Merges multiple whitespaces into a single one

    :param target: the string to clean up
    :return: the cleaned up string
    """
    return MERGE_WHITESPACES_PATTERN.sub(" ", target).strip()


def create_and_validate_query(query: Query, expected_expression: str, expected_params: list[QueryParam]):
    query_type = QueryType.get_by_value(query.query_type)

    statements = QueryBuilderFactory.construct(query_type, query.data_source_config.source_type, query).build()

    assert len(statements) == 1

    expression = merge_whitespaces(statements[0].expression)
    assert(expression == expected_expression)

    assert(statements[0].params == expected_params)