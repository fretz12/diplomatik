from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class CreateDatabaseCommand(DataSourceManagementCommand):
    """
    Command to create a logical database within the data source. The definition of a database can vary on
    implementation.
    """
    database_name: str
    """Name of the database"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.create_database, **data)
