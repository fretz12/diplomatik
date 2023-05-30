from diplomatik.data_engine.data_engine_api.query_component import QueryComponent


class LimitOffset(QueryComponent):
    """Query definition for paginating the results"""
    limit: int
    """The number of rows to limit the query result to. Equivalent to LIMIT in SQL."""

    offset: int | None = None
    """The row count to offset the results by. Equivalent to OFFSET in SQL"""
