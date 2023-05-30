from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class DeleteTableCommand(DataSourceManagementCommand):
    """Deletes a table"""
    table_name: str
    """Name of table to delete"""

    if_exists: bool = True
    """If set and the table to delete doesn't exist, no errors are thrown"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.delete_table, **data)
