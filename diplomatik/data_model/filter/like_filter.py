from typing import Literal

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field_union_type import FieldUnion


class LikeFilter(Filter):
    """
    Filter to check if a field matches a specified pattern. This is equivalent to LIKE in SQL
    """
    filter_type: Literal[FilterType.like.value]
    """The type of filter"""

    field: FieldUnion
    """The field to validate"""

    matcher: str = None
    """The pattern to match. This follows the standard SQL wild card matches. For example, in Postgres, % is used to 
    match zero or more wildcard matches. The matcher is directly passed in as a SQL expression. Its validity will 
    depend on which data source is being used."""

    negate: bool = False
    """If set, checks if a field does not match the pattern"""

    def get_filter_type(self) -> FilterType:
        return FilterType.like