from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.columns.column_definition import CreateColumnDefinition
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class AddColumnsCommand(DataSourceManagementCommand):
    """
    Command to add columns to a table
    """
    table: Table
    """The table to add columns to"""

    column_definitions: [CreateColumnDefinition]
    """Definitions on how to create columns"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.add_columns, **data)
