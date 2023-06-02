from typing import Literal

from diplomatik.data_model.query.table import Table
from diplomatik.data_model.source_formation.source_formation import SourceFormation, SourceFormationType


class SingleTableFormation(SourceFormation):
    """Definition on forming a single table"""
    formation_type: Literal[SourceFormationType.single_table.value]
    """The type of source formation"""

    table: Table
    """The table definition"""

