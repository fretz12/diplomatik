from typing import Literal

from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class TableExistsCommand(DataSourceManagementCommand):
    """Checks if a table exists"""
    command_type: Literal[DataSourceManagementCommandType.table_exists.value]
    """The type of command"""

    table: Table
    """The table to check for"""
