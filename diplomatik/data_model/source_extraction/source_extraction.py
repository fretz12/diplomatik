from abc import ABC
from enum import Enum
from pydantic import BaseModel

from diplomatik.data_model.filter.nested_filters import AndFilter, OrFilter
from diplomatik.data_model.filter.filter_union_type import FilterUnion
from diplomatik.data_model.source_extraction.order_by import OrderByMultiple
from diplomatik.exceptions.exceptions import DataModelException


class SourceExtractionType(Enum):
    """
    The type of source extraction
    """
    select = 'select'
    aggregate = 'aggregate'

    @classmethod
    def get_by_value(cls, value: str):
        """
        Gets the source extraction type based on its string value

        :param value: the value to match
        :return: the source extraction type
        """
        for type in SourceExtractionType:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid source extraction type")


class SourceExtraction(BaseModel, ABC):
    """
    Data model defining how data should be extracted from a source
    """
    filter: FilterUnion | AndFilter | OrFilter | None = None
    """Optional filter to apply to source extraction"""

    order_by: OrderByMultiple = None
    """Orders the results according to the order by definitions, sorted in the order they are defined. Equivalent to 
    ORDER BY in SQL"""
