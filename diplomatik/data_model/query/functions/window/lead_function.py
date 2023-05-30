from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType
from diplomatik.data_model.source_extraction.order_by import OrderBy


class LeadFunction(Function):
    """
    Function that returns the leading row in front of the current row. This is a convenient wrapper for a window
    function to get the leading member within a window.
    """
    field: Field
    """The field to get the leading row of"""

    rows: int
    """The number of rows in front of the current row to sample"""

    grouped_columns: [Column]
    """The columns on how to group the rows together, equivalent to a PARTITION BY in SQL"""

    order_by: [OrderBy]
    """The definitions on how to order the rows within a group"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.window, function_type=FunctionType.lead,
                         alias=alias, **data)
