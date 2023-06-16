from typing import Any, Literal

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field_union_type import FieldUnion


class InFilter(Filter):
    """
    Filters that checks if the field matches any within a specified list
    """
    filter_type: Literal[FilterType.matches_any_in.value]
    """The type of filter"""

    field: FieldUnion
    """The field to validate"""

    in_values: list[Any]
    """List of values to match against"""

    negate: bool = False
    """If set, checks if a field does not match any value in the list"""

    def get_filter_type(self) -> FilterType:
        return FilterType.matches_any_in
