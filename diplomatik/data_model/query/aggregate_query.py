from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction


class AggregateQuery(Query):
    """
    Query that aggregates rows into a single result
    """
    source_extraction: SourceExtraction
    """Definition on how to extract the data source"""

    filter: Filter | None = None
    """Optional filter to apply before aggregation"""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: [EventHook] = None, **data):
        super().__init__(query_type=QueryType.aggregate,
                         data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)

