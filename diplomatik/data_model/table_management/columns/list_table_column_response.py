from diplomatik.data_model.table_management.data_source_management_command_response import \
    DataSourceManagementCommandResponse, DataSourceManagementCommandResponseType


class ListDataSourceColumnResponse(DataSourceManagementCommandResponse):
    """TODO Data source management command response for listing a table's columns"""
    column_name: str
    data_type: str
    is_indexed: bool = False

    def __init__(self, **data):
        super().__init__(response_type=DataSourceManagementCommandResponseType.list_columns, **data)
