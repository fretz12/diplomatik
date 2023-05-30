from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field import Field


class EqualsFilter(Filter):
    """
    Filter to check for equality
    """
    lhs: Field
    """The left hand side's field for the equation"""

    rhs: Field
    """The right hand side's field for the equation"""

    negate: bool = False
    """True to compare not equals"""

    def __init__(self, **data):
        super().__init__(filter_type=FilterType.equals, **data)
