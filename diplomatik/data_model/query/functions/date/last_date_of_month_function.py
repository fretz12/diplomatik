from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType


class LastDateOfMonthFunction(Function):
    """Function that returns the last date of the month"""
    field: Field
    """The field to get the last date of the month for"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.datetime, function_type=FunctionType.last_date_of_month,
                         alias=alias, **data)
