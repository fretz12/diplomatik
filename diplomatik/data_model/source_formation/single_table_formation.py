from diplomatik.data_model.query.table import Table
from diplomatik.data_model.source_formation.source_formation import SourceFormation, SourceFormationType


class SingleTableFormation(SourceFormation):
    """Definition on forming a single table"""
    table: Table
    """The table definition"""

    def __init__(self, **data):
        super().__init__(formation_type=SourceFormationType.single_table, **data)
