from diplomatik.data_model.query.table import Table
from diplomatik.data_model.table_management.columns.column_index_definition import ColumnIndexDefinition
from diplomatik.data_model.table_management.data_source_management_command import DataSourceManagementCommand, \
    DataSourceManagementCommandType


class AddColumnIndexesCommand(DataSourceManagementCommand):
    """
    Adds indexes to columns within a table
    """
    table: Table
    """The table to index"""

    column_indexes: list[ColumnIndexDefinition]
    """Definitions on how to index the columns"""

    def __init__(self, **data):
        super().__init__(command_type=DataSourceManagementCommandType.add_column_indexes, **data)
