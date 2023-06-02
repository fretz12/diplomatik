from typing import Any

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field import Field


class InFilter(Filter):
    """
    Filters that checks if the field matches any within a specified list
    """
    field: Field
    """The field to validate"""

    in_values: list[Any]
    """List of values to match against"""

    negate: bool = False
    """If set, checks if a field does not match any value in the list"""

    def __init__(self, **data):
        super().__init__(filter_type=FilterType.matches_any_in, **data)
