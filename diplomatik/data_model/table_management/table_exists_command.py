from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class TableExistsCommand(DataSourceManagementCommand):
    """Checks if a table exists"""
    table: Table
    """The table to check for"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.table_exists, **data)
