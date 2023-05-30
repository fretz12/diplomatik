from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.materialized_result import MaterializedResult
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig
from diplomatik.data_model.query.search_query import SearchQuery


class UnionQuery(Query):
    """
    The query definition to union together subqueries

    :param select_queries: the sub-select queries to union together
    :param remove_duplicates: true to remove duplicate rows after unioning
    :param as_new_table: true to persist the results as a new table
    :param as_new_view: true to persist the results as a new view
    """
    select_queries: [SearchQuery]
    """The results of the select queries to union together"""

    remove_duplicates: bool = False
    """True to remove duplicates when unioning the outputs. Equivalent to UNION ALL in SQL if set."""

    materialized_result: MaterializedResult | None = None
    """If provided, materializes the result as defined"""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: [EventHook] = None, **data):
        super().__init__(query_type=QueryType.union,
                         data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)

