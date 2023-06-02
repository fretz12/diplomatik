from typing import Literal

from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig
from diplomatik.data_model.query.table import Table
from diplomatik.data_model.source_formation.source_formation import SourceFormation


class DeleteQuery(Query):
    """
    Query to delete data
    """
    query_type: Literal[QueryType.delete.value]
    """The type of query"""

    source_formation: SourceFormation
    """the definition on the table(s) to delete from"""

    filter: Filter | None = None
    """Condition on which to delete rows"""

    delete_from_tables: list[Table] | None = None
    """Declaration of which tables to delete from. This can be different from source formation. For example, we can 
    join multiple tables but only delete from one table."""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: list[EventHook] | None = None, **data):
        super().__init__(data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)
