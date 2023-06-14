from typing import Literal

from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class DeleteColumnIndexesCommand(DataSourceManagementCommand):
    """Deletes indexes if they exist in a table. If the specified columns have no index, then no error is thrown"""
    command_type: Literal[DataSourceManagementCommandType.delete_column_indexes.value]

    table: Table
    """The table to delete indexes"""

    columns_to_unindex: list[Column]
    """The columns to delete indexes for"""
