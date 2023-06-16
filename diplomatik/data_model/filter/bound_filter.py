from typing import Literal

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field_union_type import FieldUnion


class BoundFilter(Filter):
    """Filter that compares whether a field is within provided bounds"""
    filter_type: Literal[FilterType.bound.value]
    """The type of filter"""

    field: FieldUnion
    """The field to do the comparison for"""

    lower: FieldUnion | None = None
    """The lower bound of the filter. For example, lower < field"""

    lower_strict: bool = False
    """If set, then lower < field, else lower <= field"""

    upper: FieldUnion | None = None
    """The upper bound of the filter. For example, upper > field"""

    upper_strict: bool = False
    """If set, then upper > field, else upper >= field"""

    def get_filter_type(self) -> FilterType:
        return FilterType.bound
