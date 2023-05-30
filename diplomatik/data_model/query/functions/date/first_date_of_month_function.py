from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType


class FirstDateOfMonthFunction(Function):
    """Function that returns the first date of the month"""
    field: Field
    """The field to get the first date of the month for"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.datetime, function_type=FunctionType.first_date_of_month,
                         alias=alias, **data)

