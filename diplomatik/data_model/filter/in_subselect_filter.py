from typing import Literal, Any

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field_union_type import FieldUnion


class InSubSelectFilter(Filter):
    """
    Filters that checks if the field matches any within a select query result
    """
    filter_type: Literal[FilterType.matches_any_in_subselect.value]
    """The type of filter"""

    field: FieldUnion
    """The field to validate"""

    select_extraction: Any = None ##TODO Use Validators
    """The selection of data to compare field matches against. The data type is SelectExtraction, but we must convert 
    it with Pydantic validators to avoid circular imports"""

    negate: bool = False
    """If set, checks if a field does not match any value in the selction"""

    def get_filter_type(self) -> FilterType:
        return FilterType.matches_any_in_subselect
