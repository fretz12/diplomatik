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

    def test_select_with_bound_lower_value_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "bound",
            "field": {
                "field_type": "column",
                "column_name": "column1"
            },
            "lower": {
                "field_type": "value",
                "expression": "10"
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
                                  'WHERE ("column1" >= __param_placeholder__)',
                                  [QueryParam(value='10')])

    def test_select_with_bound_lower_strict_value_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "bound",
            "field": {
                "field_type": "column",
                "column_name": "column1"
            },
            "lower": {
                "field_type": "value",
                "expression": "10"
            },
            "lower_strict": "true"
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
                                  'WHERE ("column1" > __param_placeholder__)',
                                  [QueryParam(value='10')])

    def test_select_with_bound_upper_value_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "bound",
            "field": {
                "field_type": "column",
                "column_name": "column1"
            },
            "upper": {
                "field_type": "value",
                "expression": "10"
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
                                  'WHERE ("column1" <= __param_placeholder__)',
                                  [QueryParam(value='10')])

    def test_select_with_bound_upper_strict_value_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "bound",
            "field": {
                "field_type": "column",
                "column_name": "column1"
            },
            "upper": {
                "field_type": "value",
                "expression": "10"
            },
            "upper_strict": "true"
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
                                  'WHERE ("column1" < __param_placeholder__)',
                                  [QueryParam(value='10')])

    def test_select_with_bound_between_value_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "bound",
            "field": {
                "field_type": "column",
                "column_name": "column1"
            },
            "lower": {
                "field_type": "value",
                "expression": "5"
            },
            "upper": {
                "field_type": "value",
                "expression": "10"
            },
            "upper_strict": "true"
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
                                  'WHERE ("column1" >= __param_placeholder__ AND "column1" < __param_placeholder__)',
                                  [QueryParam(value='5'), QueryParam(value='10')])

    def test_select_with_bound_between_column_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "column1"
            }
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "bound",
            "field": {
                "field_type": "column",
                "column_name": "column1"
            },
            "lower": {
                "field_type": "column",
                "column_name": "column2"
            },
            "upper": {
                "field_type": "value",
                "expression": "10"
            },
            "upper_strict": "true"
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
                                  'WHERE ("column1" >= "column2" AND "column1" < __param_placeholder__)',
                                  [QueryParam(value='10')])

    def test_select_with_null_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "null_check",
            "field": {
                "field_type": "column",
                "column_name": "str_column"
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ("str_column" IS NULL)', [])

    def test_select_with_not_null_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "null_check",
            "field": {
                "field_type": "column",
                "column_name": "str_column"
            },
            "negate": True
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ("str_column" IS NOT NULL)', [])

    def test_select_with_like_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "like",
            "field": {
                "field_type": "column",
                "column_name": "str_column"
            },
            "matcher": "%ABC%"
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ("str_column" LIKE __param_placeholder__)',
                                  [QueryParam(value="%ABC%")])

    def test_select_with_not_like_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "like",
            "field": {
                "field_type": "column",
                "column_name": "str_column"
            },
            "matcher": "%ABC%",
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ("str_column" NOT LIKE __param_placeholder__)',
                                  [QueryParam(value="%ABC%")])

    def test_select_with_in_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "matches_any_in",
            "field": {
                "field_type": "column",
                "column_name": "str_column"
            },
            "in_values": [
                "A",
                "B"
            ]
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ("str_column" IN (__param_placeholder__, __param_placeholder__))',
                                  [QueryParam(value="A"), QueryParam(value="B")])

    def test_select_with_not_in_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "matches_any_in",
            "field": {
                "field_type": "column",
                "column_name": "str_column"
            },
            "in_values": [
                "A",
                "B"
            ],
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ("str_column" NOT IN (__param_placeholder__, __param_placeholder__))',
                                  [QueryParam(value="A"), QueryParam(value="B")])

    def test_select_with_in_subselect_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "matches_any_in_subselect",
            "field": {
                "field_type": "column",
                "column_name": "str_column"
            },
            "select_extraction": {
                "extraction_type": "select",
                "source_formation": {
                    "formation_type": "single_table",
                    "table": {
                        "table_name": "lookup_table1"
                    }
                },
                "fields": [
                    {
                        "field_type": "column",
                        "column_name": "lookup_id"
                    }
                ]
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE "str_column" IN '
                                  '(SELECT DISTINCT "lookup_id" FROM "lookup_table1" )',
                                  [])
    def test_select_with_not_in_subselect_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "matches_any_in_subselect",
            "field": {
                "field_type": "column",
                "column_name": "str_column"
            },
            "select_extraction": {
                "extraction_type": "select",
                "source_formation": {
                    "formation_type": "single_table",
                    "table": {
                        "table_name": "lookup_table1"
                    }
                },
                "fields": [
                    {
                        "field_type": "column",
                        "column_name": "lookup_id"
                    }
                ]
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE "str_column" NOT IN '
                                  '(SELECT DISTINCT "lookup_id" FROM "lookup_table1" )',
                                  [])

    def test_select_with_and_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "and",
            "filters": [
                {
                    "filter_type": "equals",
                    "lhs": {
                        "field_type": "column",
                        "column_name": "str_column"
                    },
                    "rhs": {
                        "field_type": "value",
                        "expression": "A"
                    }
                },
                {
                    "filter_type": "equals",
                    "lhs": {
                        "field_type": "column",
                        "column_name": "decimal_column"
                    },
                    "rhs": {
                        "field_type": "value",
                        "expression": "10"
                    }
                }
            ]
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ( ("decimal_column" = __param_placeholder__) AND '
                                  '("str_column" = __param_placeholder__) )',
                                  [QueryParam(value='10'), QueryParam(value='A')])

    def test_select_with_or_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "or",
            "filters": [
                {
                    "filter_type": "equals",
                    "lhs": {
                        "field_type": "column",
                        "column_name": "str_column"
                    },
                    "rhs": {
                        "field_type": "value",
                        "expression": "A"
                    }
                },
                {
                    "filter_type": "equals",
                    "lhs": {
                        "field_type": "column",
                        "column_name": "decimal_column"
                    },
                    "rhs": {
                        "field_type": "value",
                        "expression": "10"
                    }
                }
            ]
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ( ("decimal_column" = __param_placeholder__) OR '
                                  '("str_column" = __param_placeholder__) )',
                                  [QueryParam(value='10'), QueryParam(value='A')])


    def test_select_with_nested_and_or_filter(self, search_query_fixture):
        fields = [
            {
                "field_type": "column",
                "column_name": "str_column"
            },
            {
                "field_type": "column",
                "column_name": "decimal_column"
            },
        ]
        fields = json.dumps(fields)

        filter = {
            "filter_type": "or",
            "filters": [
                {
                    "filter_type": "equals",
                    "lhs": {
                        "field_type": "column",
                        "column_name": "str_column"
                    },
                    "rhs": {
                        "field_type": "value",
                        "expression": "A"
                    }
                },
                {
                    "filter_type": "and",
                    "filters": [
                        {
                            "filter_type": "equals",
                            "lhs": {
                                "field_type": "column",
                                "column_name": "str_column"
                            },
                            "rhs": {
                                "field_type": "value",
                                "expression": "B"
                            }
                        },
                        {
                            "filter_type": "equals",
                            "lhs": {
                                "field_type": "column",
                                "column_name": "decimal_column"
                            },
                            "rhs": {
                                "field_type": "value",
                                "expression": "20"
                            }
                        }
                    ]
                }
            ]
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
                                  'SELECT "str_column", "decimal_column" '
                                  'FROM "table1" '
                                  'WHERE ( ( ("decimal_column" = __param_placeholder__) AND ("str_column" = __param_placeholder__) ) OR ("str_column" = __param_placeholder__) )',
                                  [QueryParam(value='20'), QueryParam(value='B'), QueryParam(value='A')])