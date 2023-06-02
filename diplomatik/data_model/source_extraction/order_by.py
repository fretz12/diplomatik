from enum import Enum

from diplomatik.data_model.query_component import QueryComponent, QueryComponentType
from diplomatik.data_model.query.field import Field
from diplomatik.exceptions.exceptions import DataModelException


class SortType(Enum):
    ascending = 'asc'
    descending = 'desc'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the sort type based on its string value

        :param value: the value to match
        :return: the sort type
        """
        for sort in SortType:
            if sort.value == value:
                return sort

        raise DataModelException("Invalid sort type")


class OrderBy(QueryComponent):
    """
    Definition to order the results. Equivalent to ORDER BY in SQL.
    """
    field: Field
    """The field to order by"""

    sort_type: SortType = SortType.ascending
    """The sorting mode to apply on the results"""

    def __init__(self, **data):
        super().__init__(component_type=QueryComponentType.order_by, **data)


class OrderByMultiple(QueryComponent):
    """
    Definitions to jointly order the results. Equivalent to ORDER BY in SQL.
    """
    order_by: list[OrderBy]
    """The fields to order by. The order of the members determine the priority of the fields to sort by."""

    def __init__(self, **data):
        super().__init__(component_type=QueryComponentType.order_by_multiple, **data)
