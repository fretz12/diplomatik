import json

from diplomatik.tests.test_utils import create_and_validate_query
from diplomatik.tests.test_data_engine.fixtures.common_query_fixtures import management_query_fixture ## NEEDED, DO NOT REMOVE


class TestDataSourceManagementQueryBuilder:
    def test_create_table(self, management_query_fixture):
        command = {
            "command_type": "create_table",
            "table_name": "my_new_table",
            "column_definitions": [
                {
                    "column_name": "id",
                    "data_type": "auto_increment_int",
                    "extra_definitions": "PRIMARY KEY"
                },
                {
                    "column_name": "str_column",
                    "data_type": "string",
                    "byte_count": 255
                },
                {
                    "column_name": "int_column",
                    "data_type": "int32",
                    "extra_definitions": "NOT NULL"
                }
            ]
        }

        command = json.dumps(command)

        args = {
            "source_type": "postgres",
            "command": command
        }

        query = management_query_fixture("test_data_source_management_query/data_source_management_query.json", args)

        create_and_validate_query(query,
                                  'CREATE TABLE IF NOT EXISTS my_new_table '
                                  '(id SERIAL PRIMARY KEY, str_column VARCHAR(255) , int_column INT NOT NULL)', [])
