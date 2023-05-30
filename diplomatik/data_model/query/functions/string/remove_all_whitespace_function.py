from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType


class RemoveAllWhitespaceFunction(Function):
    """Removes all whitespaces from a field"""
    field: Field
    """The field to remove whitespaces for"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.string, function_type=FunctionType.remove_all_whitespace,
                         alias=alias, **data)
