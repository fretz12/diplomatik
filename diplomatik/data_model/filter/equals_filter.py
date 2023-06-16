from typing import Literal

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field_union_type import FieldUnion


class EqualsFilter(Filter):
    """
    Filter to check for equality
    """
    filter_type: Literal[FilterType.equals.value]
    """The type of filter"""

    lhs: FieldUnion
    """The left hand side's field for the equation"""

    rhs: FieldUnion
    """The right hand side's field for the equation"""

    negate: bool = False
    """True to compare not equals"""

    def get_filter_type(self) -> FilterType:
        return FilterType.equals
