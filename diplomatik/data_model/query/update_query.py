from typing import Literal

from pydantic import BaseModel

from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig
from diplomatik.data_model.query.table import Table
from diplomatik.data_model.source_formation.source_formation import SourceFormation


class UpdateCondition(BaseModel):
    """
    The condition for updating data
    """
    column: Column
    """The column to update"""

    update_to_field: Field
    """The field to update the column to, which could be another column, a value, or a function output"""


class UpdateQuery(Query):
    """
    Query to update data
    """
    query_type: Literal[QueryType.update.value]
    """The type of query"""

    update_conditions: list[UpdateCondition]
    """Conditions to update the data"""

    tables: list[Table] | None = None
    """The tables to be updated, which need to be explicitly defined here"""

    join_source_formation: SourceFormation | None = None
    """The definition in which to form the data to update. For example, it could be a joined or single table."""

    filter: Filter | None = None
    """Optional filter to apply before updating the data"""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: list[EventHook] | None = None, **data):
        super().__init__(data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)
