from typing import Literal

from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class RenameTableCommand(DataSourceManagementCommand):
    """
    Renames a table
    """
    command_type: Literal[DataSourceManagementCommandType.rename_table.value]
    """The type of command"""

    from_table: Table
    """The table to rename"""

    to_table: Table
    """The new table to rename to"""
