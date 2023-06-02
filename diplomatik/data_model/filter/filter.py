from enum import Enum

from diplomatik.data_model.query_component import QueryComponent, QueryComponentType
from diplomatik.exceptions.exceptions import DataModelException


class FilterType(Enum):
    """
    The type of filter
    """
    equals = 'equals'
    """Filter checking if two fields are equal"""

    null_check = 'null_check'
    """Checks if a field is null"""

    like = 'like'
    """Wildcard matches, equivalent to LIKE in SQL"""

    matches_any_in = 'matches_any_in'
    """Checks if the field matches any value in a list of values. Equivalent to IN in SQL"""

    matches_any_in_subselect = 'matches_any_in_subselect'
    """Checks if a field matches any within the output of a select query. Equivalent to a nested sub-select in SQL"""

    bound = 'bound'
    """Checks if a field is within the bounds of provided limints, i.e., >, <, >=, <="""

    and_condition = 'and'
    """Combines multiple filters via an AND relationship"""

    or_condition = 'or'
    """Combines multiple filters via an OR relationship"""

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the filter type based on its string value

        :param value: the value to match
        :return: the filter type
        """
        for filter in FilterType:
            if filter.value == value:
                return filter

        raise DataModelException(f"{value} is not a valid filter")


class Filter(QueryComponent):
    """"The base filter class"""
    filter_type: FilterType
    """The type of filter"""

    def __init__(self, **data):
        super().__init__(component_type=QueryComponentType.filter, **data)