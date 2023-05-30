from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType
from diplomatik.data_model.source_extraction.order_by import OrderBy


class LastInGroupFunction(Function):
    """
    Function that returns the last value in a group. This is a convenient wrapper for a window function to get the
    last member within a window.
    """
    field: Field
    """The field to get the last row of"""

    grouped_columns: [Column]
    """The columns on how to group the rows together, equivalent to a PARTITION BY in SQL"""

    order_by: [OrderBy]
    """The definitions on how to order the rows within a group"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.window, function_type=FunctionType.last_in_group,
                         alias=alias, **data)