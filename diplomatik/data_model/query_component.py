from abc import ABC
from enum import Enum

from pydantic import BaseModel


class QueryComponentType(Enum):
    """The type of query component"""

    aggregation = 'aggregation'
    column = 'column'
    filter = 'filter'
    function = 'function'
    group_by = 'group_by'
    limit_offset = 'limit_offset'
    order_by = 'order_by'
    order_by_multiple = 'order_by_multiple'
    source_formation = 'source_formation'
    table = 'table'
    value = 'value'
    view = 'view'
    window_aggregation = 'window_aggregation'
    window_bound = 'window_bound'


class QueryComponent(ABC, BaseModel):
    """
    The base query component which we can build partial statements from
    """
    component_type: QueryComponentType
    """The type of component"""
