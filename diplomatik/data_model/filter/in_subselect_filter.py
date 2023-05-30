from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field import Field
from diplomatik.data_model.source_extraction.select_extraction import SelectExtraction


class InSubSelectFilter(Filter):
    """
    Filters that checks if the field matches any within a select query result
    """
    field: Field
    """The field to validate"""

    select_extraction: SelectExtraction = None
    """The selection of data to compare field matches against"""

    negate: bool = False
    """If set, checks if a field does not match any value in the selction"""

    def __init__(self, **data):
        super().__init__(command_type=FilterType.matches_any_in_subselect, **data)
