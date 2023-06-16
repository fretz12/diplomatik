from typing import Literal

from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class CreateDatabaseCommand(DataSourceManagementCommand):
    """
    Command to create a logical database within the data source. The definition of a database can vary on
    implementation.
    """
    command_type: Literal[DataSourceManagementCommandType.create_database.value]
    """The type of command"""

    database_name: str
    """Name of the database"""
