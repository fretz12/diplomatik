from typing import Literal, ForwardRef

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.filter.filter_union_type import FilterUnion

AndFilter = ForwardRef('AndFilter')
OrFilter = ForwardRef('OrFilter')


class AndFilter(Filter):
    """The filter the outputs the logical AND of its children filters"""
    filter_type: Literal[FilterType.and_condition.value]
    """The type of filter"""

    filters: list[FilterUnion | AndFilter | OrFilter]
    """The sub-filters to AND together"""

    def get_boolean_operator_expression(self) -> str:
        return 'AND'

    def get_filter_type(self) -> FilterType:
        return FilterType.and_condition

    def get_children_filters(self) -> list[FilterUnion | AndFilter] | None:
        return self.filters


class OrFilter(Filter):
    """The filter the outputs the logical OR of its children filters"""
    filter_type: Literal[FilterType.or_condition.value]
    """The type of filter"""

    filters: list[FilterUnion | OrFilter | AndFilter]
    """The sub-filters to OR together"""

    def get_boolean_operator_expression(self) -> str:
        return 'OR'

    def get_filter_type(self) -> FilterType:
        return FilterType.or_condition

    def get_children_filters(self) -> list[FilterUnion | OrFilter] | None:
        return self.filters


AndFilter.update_forward_refs()
OrFilter.update_forward_refs()
