import json

from diplomatik.data_model.query.query_statement import QueryParam
from diplomatik.tests.test_utils import create_and_validate_query
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

        query = search_query_fixture("test_search_query/search_query_select_fields.json", args)

        create_and_validate_query(query, 'SELECT "column1", "table1"."column2", "column3" AS alias3 FROM "table1"', [])

    def test_select_values(self, search_query_fixture):
        fields = [
            {
                'field_type': 'value',
                "expression": "ABC",
                "alias": "alias1"
            },
            {
                'field_type': 'value',
                "expression": "10",
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

        query = search_query_fixture("test_search_query/search_query_select_fields.json", args)

        create_and_validate_query(
            query,
            'SELECT __param_placeholder__ as alias1, __param_placeholder__ as alias2, "column1" / 100 as alias3 '
            'FROM "table1"',
            [QueryParam(value='ABC'), QueryParam(value='10')])

    def test_select_columns_with_join(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column",
                "table_name": "table1"
            },
            {
                "field_type": "column",
                "column_name": "lookup_attr1",
                "table_name": "lookup_table1"
            }
        ]
        fields = json.dumps(fields)

        right_tables = [
            {
                "join_type": "inner",
                "table": {
                    "table_name": "lookup_table1"
                },
                "on_condition": {
                    "filter_type": "equals",
                    "lhs": {
                        "field_type": "column",
                        "column_name": "str_column",
                        "table_name": "table1"
                    },
                    "rhs": {
                        "field_type": "column",
                        "column_name": "lookup_id",
                        "table_name": "lookup_table1"
                    }
                }
            }
        ]
        right_tables = json.dumps(right_tables)

        args = {
            "source_type": "postgres",
            "left_table_name": "table1",
            "right_tables": right_tables,
            "fields": fields
        }

        query = search_query_fixture("test_search_query/search_query_select_fields_with_join.json", args)

        create_and_validate_query(query,
                                  'SELECT "table1"."str_column", "lookup_table1"."lookup_attr1" '
                                  'FROM "table1" '
                                  'inner JOIN "lookup_table1" ON '
                                  '("table1"."str_column" = "lookup_table1"."lookup_id")', [])
