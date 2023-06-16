import json

from diplomatik.data_model.query.query_statement import QueryParam
from diplomatik.tests.test_utils import create_and_validate_query
from diplomatik.tests.test_data_engine.fixtures.common_query_fixtures import insert_query_fixture ## NEEDED, DO NOT REMOVE


class TestSearchQueryBuilder:
    def test_insert_values(self, insert_query_fixture):
        columns = [
            {
                'field_type': 'column',
                "column_name": "str_column"
            },
            {
                'field_type': 'column',
                "column_name": "int_column"
            }
        ]
        columns = json.dumps(columns)

        values = [
            [
                "A",
                10
            ],
            [
                "B",
                20
            ],
            [
                "C",
                30
            ]
        ]
        values = json.dumps(values)

        args = {
            "source_type": "postgres",
            "table_name": "table1",
            "columns": columns,
            "values": values
        }

        query = insert_query_fixture("test_insert_query/test_insert_values_query.json", args)

        create_and_validate_query(query,
                                  'INSERT INTO "table1" ("str_column", "int_column") '
                                  'VALUES(__param_placeholder__, __param_placeholder__)',
                                  [QueryParam(value=['A', 'B', 'C']),
                                   QueryParam(value=[10, 20, 30])])
