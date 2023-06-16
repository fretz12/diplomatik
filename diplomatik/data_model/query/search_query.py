from typing import Literal

from pydantic import Field

from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.materialized_result import MaterializedResult
from diplomatik.data_model.query.query import Query, DataSourceConfig, QueryResultConfig, QueryType
from diplomatik.data_model.source_extraction.source_extraction_union_type import SourceExtractionUnion


class SearchQuery(Query):
    """
    The query for extracting data based on selections
    """
    query_type: Literal[QueryType.search.value]
    """The type of query"""

    source_extraction: SourceExtractionUnion
    """The definition for extracting the data"""

    materialized_result: MaterializedResult | None = None
    """If provided, materializes the result as defined"""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: list[EventHook] | None = None, **data):
        super().__init__(data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)
