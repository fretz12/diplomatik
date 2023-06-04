from typing import Literal

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field_union_type import FieldUnion


class NullCheckFilter(Filter):
    """Checks if a field is null"""
    filter_type: Literal[FilterType.null_check.value]
    """The type of filter"""

    field: FieldUnion
    """The field to check"""

    negate: bool = False
    """If set, checks if a field is not null"""

    empty_as_null: bool = False
    """If set, treats empty strings as null"""

    def get_filter_type(self) -> FilterType:
        return FilterType.null_check
