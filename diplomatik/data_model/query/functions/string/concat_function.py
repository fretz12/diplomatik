from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType


class ConcatFunction(Function):
    """Concatenates together multiple fields into a single string"""
    fields: [Field]
    """The fields to concatenate"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.string, function_type=FunctionType.concat,
                         alias=alias, **data)
