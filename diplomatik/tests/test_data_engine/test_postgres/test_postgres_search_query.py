import json

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder_factory import \
    QueryBuilderFactory
from diplomatik.data_model.query.query import QueryType
from diplomatik.tests.test_utils import merge_whitespaces
from diplomatik.tests.test_data_engine.fixtures.common_query_fixtures import search_query_fixture ## NEEDED, DO NOT REMOVE


class TestSearchQueryBuilder:
    def test_select_columns_no_filter(self, search_query_fixture):
        fields = [
            {
                'field_type': 'column',
                "column_name": "column1"
            },
            {
                'field_type': 'column',
                "column_name": "column2",
                "table_name": "table1"
            },
            {
                'field_type': 'column',
                "column_name": "column3",
                "alias": "alias3"
            }
        ]

        fields = json.dumps(fields)

        args = {
            "source_type": "postgres",
            "table_name": "table1",
            "fields": fields
        }

        query = search_query_fixture("test_search_query/search_query_select_fields_no_filter.json", args)

        query_type = QueryType.get_by_value(query.query_type)

        query_builder = QueryBuilderFactory.construct(query_type, query.data_source_config.source_type, query)

        statements = query_builder.build()

        assert len(statements) == 1

        expression = merge_whitespaces(statements[0].expression)
        assert(expression == 'SELECT "column1", "table1"."column2", "column3" AS alias3 FROM "table1"')

        assert(statements[0].params == [])
