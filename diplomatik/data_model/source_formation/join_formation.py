from enum import Enum
from typing import Literal

from pydantic import BaseModel

from diplomatik.data_model.filter.filter_union_type import FilterUnion
from diplomatik.data_model.filter.nested_filters import OrFilter, AndFilter
from diplomatik.data_model.query.table import Table
from diplomatik.data_model.source_formation.source_formation import SourceFormation, SourceFormationType
from diplomatik.exceptions.exceptions import DataModelException


class JoinType(Enum):
    """The type of table join"""
    inner = 'inner'
    left = 'left'
    right = 'right'
    full = 'full'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the join type by string value

        :param value: the value to match
        :return: the join type
        """
        for join_type in JoinType:
            if join_type.value == value:
                return join_type

        raise DataModelException("Invalid join type")


class RightJoinTable(BaseModel):
    """
    The tables to join to main anchored table
    """
    join_type: JoinType
    """The type of join to use"""

    table: Table
    """The table to join"""

    on_condition: FilterUnion | AndFilter | OrFilter
    """The condition defining how the tables are to be joined. Equivalent to the ON portion of a join."""


class JoinFormation(SourceFormation):
    """The definition on how to form from joined sources"""
    formation_type: Literal[SourceFormationType.join.value]
    """The type of source formation"""

    left_table: Table
    """The anchored table which other tables will join to"""

    right_tables: list[RightJoinTable]
    """The tables to join the anchored table"""

