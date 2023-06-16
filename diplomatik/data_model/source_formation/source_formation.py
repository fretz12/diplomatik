from abc import ABC
from enum import Enum

from diplomatik.data_model.query_component import QueryComponent, QueryComponentType
from diplomatik.exceptions.exceptions import DataModelException


class SourceFormationType(Enum):
    """
    The type of source formation
    """
    single_table = 'single_table'
    """Source formation as a single table"""

    join = 'join'
    """Form the source by joining multiple tables"""

    @classmethod
    def get_by_value(cls, value: str):
        """
        Gets the source formation type based on its string value

        :param value: the value to match
        :return: the source formation type
        """
        for type in SourceFormationType:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid source formation type")


class SourceFormation(QueryComponent, ABC):
    """Definition on how to create a virtual source as part of a query. Example: it defines how tables are joined
    together."""

    def __init__(self, **data):
        super().__init__(component_type=QueryComponentType.source_formation, **data)
