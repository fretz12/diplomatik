from typing import Literal

from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig
from diplomatik.data_model.table_management.data_source_management_command_union_type import \
    DataSourceManagementCommandUnion


class DataSourceManagementQuery(Query):
    """
    Query for performing management tasks in the data source
    """
    query_type: Literal[QueryType.data_source_management.value]
    """The type of query"""

    command: DataSourceManagementCommandUnion
    """The management command"""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: list[EventHook] | None = None, **data):
        super().__init__(data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)
