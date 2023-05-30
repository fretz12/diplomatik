from diplomatik.data_model.table_management.columns.column_definition import CreateColumnDefinition
from diplomatik.data_model.table_management.columns.column_index_definition import ColumnIndexDefinition
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class CreateTableCommand(DataSourceManagementCommand):
    """
    Command to create a new table
    """
    table_name: str
    """Name of the new table"""

    column_definitions: [CreateColumnDefinition]
    """Definitions on how to create the new columns"""

    column_indexes: [ColumnIndexDefinition] = None
    """Index definitions on any newly create columns"""

    if_not_exists: bool = True
    """Creates the table only if it doesn't exist, without throwing an error"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.create_table, **data)



