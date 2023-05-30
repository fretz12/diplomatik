from abc import ABC
from enum import Enum

from diplomatik.data_engine.data_engine_api.query_component import QueryComponent


class SourceFormationType(Enum):
    """
    The type of source formation
    """
    single_table = 'single_table'
    """Source formation as a single table"""

    join = 'join'
    """Form the source by joining multiple tables"""


class SourceFormation(QueryComponent, ABC):
    """Definition on how to create a virtual source as part of a query. Example: it defines how tables are joined
    together."""
    formation_type: SourceFormationType
    """The type of source formation"""
