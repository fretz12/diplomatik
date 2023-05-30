from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class RenameTableCommand(DataSourceManagementCommand):
    """
    Renames a table
    """
    from_table: Table
    """The table to rename"""

    to_table: Table
    """The new table to rename to"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.rename_table, **data)
