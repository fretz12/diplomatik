from typing import Literal

from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class DeleteColumnsCommand(DataSourceManagementCommand):
    """Delete columns in a table"""
    command_type: Literal[DataSourceManagementCommandType.delete_columns.value]
    """The type of command"""

    table: Table
    """The table from which to delete columns"""

    columns: list[Column]
    """The columns to delete"""
