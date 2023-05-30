from abc import ABC
from enum import Enum

from pydantic import BaseModel

from diplomatik.data_engine.data_engine_api.query_component import QueryComponent
from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType
from diplomatik.data_model.source_extraction.order_by import OrderBy
from diplomatik.exceptions.exceptions import DataModelException


class WindowBoundType(Enum):
    """The window bound type, equivalent to that used to define the window position in SQL window functions"""
    unbounded = 'unbounded'
    row_count = 'row_count'
    current_row = 'current_row'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the window bound type based on its string value

        :param value: the value to match
        :return: the window bound type
        """
        for type in WindowBoundType:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid window bound type")


class WindowAggregationType(Enum):
    """The window aggregation type, equivalent to how the window aggregates the rows in SQL"""
    first_value = 'first_value'
    last_value = 'last_value'
    lead = 'lead'
    lag = 'lag'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the window aggregation type based on its string value

        :param value: the value to match
        :return: the window aggregation type
        """
        for type in WindowAggregationType:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid window aggregation type")


class WindowBound(QueryComponent, ABC):
    """The window bound data model that determines how the window rolls of the rows. For more details, refer to
    window functions in SQL"""
    window_bound_type: WindowBoundType
    """The window bound type"""

    rows_count: int | None = None
    """Should be provided to indicate the number of rows preceding or following the current row"""


class WindowAggregation(QueryComponent, ABC):
    """The window aggregation base model"""
    aggregation_type: WindowAggregationType
    """The window aggregation type"""


class FirstValueWindowAggregation(WindowAggregation, BaseModel):
    """The window aggregation function to get the first value of the window. Equivalent to FIRST_VALUE in SQL."""
    field: Field
    """The field to get the first value on"""

    def __init__(self, **data):
        super().__init__(aggregation_type=WindowAggregationType.first_value, **data)


class LastValueWindowAggregation(WindowAggregation):
    """The window aggregation function to get the last value of the window. Equivalent to LAST_VALUE in SQL."""
    field: Field
    """The field to get the last value on"""

    def __init__(self, **data):
        super().__init__(aggregation_type=WindowAggregationType.last_value, **data)


class LeadWindowAggregation(WindowAggregation):
    """The window aggregation function get the leading row with respect to the current row in the window. Equivalent to
    LEAD in SQL"""
    field: Field
    """The field to get the lead value on"""
    rows: int
    """The number of rows leading the current row"""

    def __init__(self, **data):
        super().__init__(aggregation_type=WindowAggregationType.lead, **data)


class LagWindowAggregation(WindowAggregation):
    """The window aggregation function get the lagging row with respect to the current row in the window. Equivalent to
    LAG in SQL"""
    field: Field
    """The field to get the lag value on"""
    rows: int
    """The number of rows lagging the current row"""

    def __init__(self, **data):
        super().__init__(aggregation_type=WindowAggregationType.lag, **data)


class WindowFunction(Function):
    """
    The window function, equivalent to window functions in SQL
    """
    window_aggregation: WindowAggregation
    """The definition on how to aggregate the field in the window"""

    partition_by: [Column]
    """The columns to partition by for each window. Equivalent to PARTITION BY in SQL"""

    order_by: [OrderBy]
    """Defines how rows are ordered within each window. Equivalent to ORDER BY in window functions in SQL"""

    start_bound: WindowBound
    """The starting bound of the window. Equivalent to PRECEDING or CURRENT ROW in SQL"""

    end_bound: WindowBound
    """The ending bound of the window. Equivalent to FOLLOWING or CURRENT ROW in SQL"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.window, function_type=FunctionType.window, alias=alias,
                         **data)
