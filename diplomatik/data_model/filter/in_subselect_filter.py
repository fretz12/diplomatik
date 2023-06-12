from typing import Literal, Any

from pydantic import validator

from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.field_union_type import FieldUnion
from diplomatik.data_model.source_extraction.limit_offset import LimitOffset


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
    """If set, checks if a field does not match any value in the selection"""

    def get_filter_type(self) -> FilterType:
        return FilterType.matches_any_in_subselect

    @validator('select_extraction')
    def marshal(cls, v):
        """
        Manually marshals the select extraction raw dict into the model. We must convert it manually due to circular
        imports

        :param v: the raw dict
        :return: the SelectExtraction object
        """
        from diplomatik.data_model.source_extraction.select_extraction import SelectExtraction

        select_extraction = SelectExtraction(extraction_type=v['extraction_type'],
                                             source_formation=v['source_formation'],
                                             fields=v['fields'])

        if 'select_all_columns' in select_extraction:
            select_extraction.select_all_columns = v['select_all_columns']

        if 'pagination' in select_extraction:
            select_extraction.pagination = LimitOffset.parse_obj(v['pagination'])

        if 'distinct' in select_extraction:
            select_extraction.distinct = v['distinct']

        return select_extraction
