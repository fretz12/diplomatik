from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class ListColumnsCommand(DataSourceManagementCommand):
    """
    Command to get the list of columns for a table
    """
    table: Table
    """The table the list columns for"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.list_columns, **data)
