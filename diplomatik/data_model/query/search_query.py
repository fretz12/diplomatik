from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.materialized_result import MaterializedResult
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction


class SearchQuery(Query):
    """
    The query for extracting data based on selections

    :param source_extraction: the definition for extracting the source
    :param filter: any filters to apply to query
    :param query_source: the source to query
    :param query_destination: the desintation to put the results into
    :param view: if defined, the results will be created in the form of a permanent table view, supported by most
    databases
    :param as_new_table: True to create a new table from the selection
    :param query_id: ID for the query
    :param event_hooks: event hooks to process before/after this query
    """
    source_extraction: SourceExtraction
    """The definition for extracting the data"""

    filter: Filter | None = None
    """Optional filter to apply to search"""

    materialized_result: MaterializedResult | None = None
    """If provided, materializes the result as defined"""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: [EventHook] = None, **data):
        super().__init__(query_type=QueryType.search,
                         data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)
