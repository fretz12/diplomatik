from typing import Literal

from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig


class BatchQuery(Query):
    """
    A batch queries that contains sub queries to execute in order
    """
    query_type: Literal[QueryType.batch.value]
    """The type of query"""

    queries: list[Query]
    """The queries belonging to the batch"""

    execute_as_transaction: bool = True
    """True to execute all queries as a transaction, if applicable"""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: list[EventHook] | None = None, **data):
        super().__init__(data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)
