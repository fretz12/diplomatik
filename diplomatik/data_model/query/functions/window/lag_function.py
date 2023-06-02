from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType
from diplomatik.data_model.source_extraction.order_by import OrderByMultiple


class LagFunction(Function):
    """
    Function that returns the lagging row behind the current row. This is a convenient wrapper for a window function to
    get the lagging member within a window.
    """
    field: Field
    """The field to get the lagging row of"""

    rows: int
    """The number of rows behind the current row to sample"""

    grouped_columns: list[Column]
    """The columns on how to group the rows together, equivalent to a PARTITION BY in SQL"""

    order_by: OrderByMultiple
    """The definitions on how to order the rows within a group"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.window, function_type=FunctionType.lag,
                         alias=alias, **data)