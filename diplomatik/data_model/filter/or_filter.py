from diplomatik.data_model.filter.filter import Filter, FilterType


class OrFilter(Filter):
    """The filter the outputs the logical OR of its children filters"""
    filters: [Filter]
    """The sub-filters to OR together"""

    def __init__(self, **data):
        super().__init__(filter_type=FilterType.or_condition, **data)
