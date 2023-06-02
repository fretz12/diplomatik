from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class DeleteColumnIndexesCommand(DataSourceManagementCommand):
    """Deletes indexes if they exist in a table. If the specified columns have no index, then no error is thrown"""
    table: Table
    """The table to delete indexes"""

    columns_to_unindex: list[Column]
    """The columns to delete indexes for"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.delete_column_indexes, **data)
