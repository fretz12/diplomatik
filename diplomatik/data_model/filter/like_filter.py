from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field import Field


class LikeFilter(Filter):
    """
    Filter to check if a field matches a specified pattern. This is equivalent to LIKE in SQL
    """
    field: Field
    """The field to validate"""

    matcher: str = None
    """The pattern to match. This follows the standard SQL wild card matches. For example, in Postgres, % is used to 
    match zero or more wildcard matches. The matcher is directly passed in as a SQL expression. Its validity will 
    depend on which data source is being used."""

    negate: bool = False
    """If set, checks if a field does not match the pattern"""

    empty_as_null: bool = False
    """If set, it will treat blank strings as nulls"""

    def __init__(self, **data):
        super().__init__(command_type=FilterType.like, **data)
