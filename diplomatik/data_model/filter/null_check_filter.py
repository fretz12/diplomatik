from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field import Field


class NullCheckFilter(Filter):
    """Checks if a field is null"""
    field: Field
    """The field to check"""

    negate: bool = False
    """If set, checks if a field is not null"""

    empty_as_null: bool = False
    """If set, treats empty strings as null"""

    def __init__(self, **data):
        super().__init__(command_type=FilterType.null_check, **data)
