from typing import Literal

from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class ListColumnsCommand(DataSourceManagementCommand):
    """
    Command to get the list of columns for a table
    """
    command_type: Literal[DataSourceManagementCommandType.list_columns.value]
    """The type of command"""

    table: Table
    """The table the list columns for"""
