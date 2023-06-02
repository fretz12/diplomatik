from typing import Any

from pydantic import BaseModel

from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.field import FieldDataType


class QueryParam(BaseModel):
    value: Any
    key: str = ''
    data_type: FieldDataType | None = None


class QueryStatement(BaseModel):
    """
    The statement conveying how a query should be executed.
    """
    expression: str = None
    """The SQL expression to execute"""

    params: list[QueryParam] | None = None
    """Parameters associated with a prepared statement"""

    query_id: str | None = None
    """Unique, self-provided ID for this query"""

    pre_query_event_hooks: list[EventHook] | None  = None
    """Event hooks to execute before the query gets executed"""

    post_query_event_hooks: list[EventHook] | None  = None
    """Event hooks to execute after the query gets executed"""

    def extend_params(self, params: list[QueryParam] | None):
        """
        Adds a list of query parameters to the current parameters

        :param params: the parameters to add
        """
        if not params:
            return

        self.params.extend(params)


class QueryStatementTransaction(BaseModel):
    """
    The collection of query statements to execute together as a transaction. The queries will be executed in the
    order as defined in the list
    """
    statements: list[QueryStatement]
