from typing import Literal

from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class CreateTableLikeCommand(DataSourceManagementCommand):
    """Creates a new table with the same schema as another table, but with no data. This is equivalent to
    CREATE TABLE LIKE in SQL"""
    command_type: Literal[DataSourceManagementCommandType.create_table_like.value]
    """The type of command"""

    from_table: Table
    """The table to create from"""

    to_table: Table
    """The new table to create"""
