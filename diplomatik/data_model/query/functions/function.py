from enum import Enum

from diplomatik.data_engine.data_engine_api.query_component import QueryComponentType
from diplomatik.data_model.query.field import Field, FieldDataType
from diplomatik.exceptions.exceptions import DataModelException


class FunctionCategory(Enum):
    """
    The function category types
    """
    math = 'math'
    string = 'string'
    datetime = 'datetime'
    window = 'window'
    logic = 'logic'

    @classmethod
    def get_by_value(cls, value: str):
        """
        Gets the function category enum by value

        :param value: the value to get from
        :return: the matching function category
        :rtype: FunctionCategory
        """
        for category in FunctionCategory:
            if category.value == value:
                return category

        raise DataModelException(f"{value} is not a valid function category")


class FunctionType(Enum):
    ## Math
    round = 'round'
    sumif = 'sumif'

    ## String
    concat = 'concat'
    remove_all_whitespace = 'remove_all_whitespace'

    ## Date
    first_date_of_month = 'first_date_of_month'
    last_date_of_month = 'last_date_of_month'

    ## Window
    window = 'window'
    first_in_group = 'first_in_group'
    last_in_group = 'last_in_group'
    lead = 'lead'
    lag = 'lag'

    ##Logic
    case_when = 'case_when'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the function type enum by value

        :param value: the value to get from
        :return: the matching function type
        :rtype: FunctionType
        """
        for type in FunctionType:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid function type")


class Function(Field):
    function_category: FunctionCategory
    """The category the function belongs in"""

    function_type: FunctionType
    """The type of function"""

    def __init__(self, data_type: FieldDataType | None = None, alias: str | None = None, **data):
        super().__init__(component_type=QueryComponentType.function, data_type=data_type, alias=alias, **data)
