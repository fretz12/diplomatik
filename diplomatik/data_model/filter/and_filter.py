from diplomatik.data_model.filter.filter import Filter, FilterType


class AndFilter(Filter):
    """The filter the outputs the logical AND of its children filters"""
    filters: [Filter]
    """The sub-filters to AND together"""

    def __init__(self, **data):
        super().__init__(filter_type=FilterType.and_condition, **data)
