from typing import Literal

from diplomatik.data_model.table_management.columns.column_definition import CreateColumnDefinitionUnion
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class CreateTableCommand(DataSourceManagementCommand):
    """
    Command to create a new table
    """
    command_type: Literal[DataSourceManagementCommandType.create_table.value]
    """The type of command"""

    table_name: str
    """Name of the new table"""

    column_definitions: list[CreateColumnDefinitionUnion]
    """Definitions on how to create the new columns"""

    if_not_exists: bool = True
    """Creates the table only if it doesn't exist, without throwing an error"""
