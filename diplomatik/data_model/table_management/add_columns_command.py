from typing import Literal

from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.columns.column_definition import CreateColumnDefinition
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class AddColumnsCommand(DataSourceManagementCommand):
    """
    Command to add columns to a table
    """
    command_type: Literal[DataSourceManagementCommandType.add_columns.value]
    """The type of command"""

    table: Table
    """The table to add columns to"""

    column_definitions: list[CreateColumnDefinition]
    """Definitions on how to create columns"""
