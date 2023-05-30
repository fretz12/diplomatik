from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType


class RoundFunction(Function):
    """Function that rounds a number"""
    field: Field
    """The field to round"""

    decimals: int = None
    """If provided, the number of decimals to round to. If not provided, rounds to the nearest integer"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.math, function_type=FunctionType.round,
                         alias=alias, **data)

