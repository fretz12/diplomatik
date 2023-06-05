import json

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder_factory import \
    QueryBuilderFactory
from diplomatik.data_model.query.query import QueryType
from diplomatik.data_model.query.query_statement import QueryParam
from diplomatik.data_model.query.search_query import SearchQuery
from diplomatik.tests.test_utils import merge_whitespaces
from diplomatik.tests.test_data_engine.fixtures.common_query_fixtures import search_query_fixture ## NEEDED, DO NOT REMOVE


class TestSearchQueryBuilder:
    def test_select_columns(self, search_query_fixture):
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

        self.__create_and_validate_query(
            query, 'SELECT "column1", "table1"."column2", "column3" AS alias3 FROM "table1"', [])

    def test_select_values(self, search_query_fixture):
        fields = [
            {
                'field_type': 'value',
                "expression": "ABC",
                "alias": "alias1"
            },
            {
                'field_type': 'value',
                "expression": "1 + 2",
                "alias": "alias2"
            },
            {
                'field_type': 'value',
                "expression": "__field_placeholder__ / 100",
                "fields": [
                    {
                        'field_type': 'column',
                        "column_name": "column1"
                    }
                ],
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

        self.__create_and_validate_query(
            query,
            'SELECT __param_placeholder__ as alias1, 1 + 2 as alias2, "column1" / 100 as alias3 FROM "table1"',
            [QueryParam(value='ABC')])


    def __create_and_validate_query(self, query: SearchQuery, expected_expression: str,
                                    expected_params: list[QueryParam]):
        query_type = QueryType.get_by_value(query.query_type)

        statements = QueryBuilderFactory.construct(query_type, query.data_source_config.source_type, query).build()

        assert len(statements) == 1

        expression = merge_whitespaces(statements[0].expression)
        assert(expression == expected_expression)

        assert(statements[0].params == expected_params)