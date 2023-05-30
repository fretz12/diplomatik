from typing import Collection

from pydantic import BaseModel

from diplomatik.data_model.query.event_hooks.event_hook import EventHook


class QueryStatement(BaseModel):
    """
    The statement conveying how a query should be executed.
    """
    expression: str = None
    """The SQL expression to execute"""

    params: Collection | None = None
    """Parameters associated with a prepared statement"""

    query_id: str | None = None
    """Unique, self-provided ID for this query"""

    pre_query_event_hooks: [EventHook] = None
    """Event hooks to execute before the query gets executed"""

    post_query_event_hooks: [EventHook] = None
    """Event hooks to execute after the query gets executed"""


class QueryStatementTransaction(BaseModel):
    """
    The collection of query statements to execute together as a transaction. The queries will be executed in the
    order as defined in the list
    """
    statements: [QueryStatement]
