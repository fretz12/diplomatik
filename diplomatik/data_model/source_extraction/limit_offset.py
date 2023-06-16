from diplomatik.data_model.query_component import QueryComponent, QueryComponentType


class LimitOffset(QueryComponent):
    """Query definition for paginating the results"""
    limit: int
    """The number of rows to limit the query result to. Equivalent to LIMIT in SQL."""

    offset: int | None = None
    """The row count to offset the results by. Equivalent to OFFSET in SQL"""

    def __init__(self, **data):
        super().__init__(component_type=QueryComponentType.limit_offset, **data)