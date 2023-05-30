from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field import Field


class BoundFilter(Filter):
    """Filter that compares whether a field is within provided bounds"""
    field: Field
    """The field to do the comparison for"""

    lower: Field | None = None
    """The lower bound of the filter. For example, lower < field"""

    lower_strict: bool = False
    """If set, then lower < field, else lower <= field"""

    upper: Field | None = None
    """The upper bound of the filter. For example, upper > field"""

    upper_strict: bool = False
    """If set, then upper > field, else upper >= field"""

    def __init__(self, **data):
        super().__init__(filter_type=FilterType.bound, **data)
