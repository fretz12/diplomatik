import json

from diplomatik.data_model.query.query_statement import QueryParam
from diplomatik.tests.test_utils import create_and_validate_query
from diplomatik.tests.test_data_engine.fixtures.common_query_fixtures import search_query_fixture ## NEEDED, DO NOT REMOVE


class TestSearchQueryWithFilter:
    def test_select_with_equals_columns_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "equals",
            "lhs": {
                "field_type": "column",
                "column_name": "column1"
            },
            "rhs": {
                "field_type": "column",
                "column_name": "column2"
            }
        }
        filter = json.dumps(filter)

        args = {
            "source_type": "postgres",
            "table_name": "table1",
            "fields": fields,
            "filter": filter
        }

        query = search_query_fixture("test_search_query/search_query_select_fields.json", args)

        create_and_validate_query(query,
                                  'SELECT "column1" '
                                  'FROM "table1" '
                                  'WHERE ("column1" = "column2")', [])

    def test_select_with_not_equals_columns_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "equals",
            "lhs": {
                "field_type": "column",
                "column_name": "column1"
            },
            "rhs": {
                "field_type": "column",
                "column_name": "column2"
            },
            "negate": "true"
        }
        filter = json.dumps(filter)

        args = {
            "source_type": "postgres",
            "table_name": "table1",
            "fields": fields,
            "filter": filter
        }

        query = search_query_fixture("test_search_query/search_query_select_fields.json", args)

        create_and_validate_query(query,
                                  'SELECT "column1" '
                                  'FROM "table1" '
                                  'WHERE ("column1" <> "column2")', [])


    def test_select_with_equals_value_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "equals",
            "lhs": {
                "field_type": "column",
                "column_name": "column1"
            },
            "rhs": {
                "field_type": "value",
                "expression": "ABC"
            }
        }
        filter = json.dumps(filter)

        args = {
            "source_type": "postgres",
            "table_name": "table1",
            "fields": fields,
            "filter": filter
        }

        query = search_query_fixture("test_search_query/search_query_select_fields.json", args)

        create_and_validate_query(query,
                                  'SELECT "column1" '
                                  'FROM "table1" '
                                  'WHERE ("column1" = __param_placeholder__)',
                                  [QueryParam(value='ABC')])