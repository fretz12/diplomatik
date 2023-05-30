from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class DeleteColumnsCommand(DataSourceManagementCommand):
    """Delete columns in a table"""
    table: Table
    """The table from which to delete columns"""

    columns: [Column]
    """The columns to delete"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.delete_columns, **data)
