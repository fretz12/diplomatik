from pydantic import BaseModel

from diplomatik.data_model.query.column import Column


class ColumnIndexDefinition(BaseModel):
    """Definition on how to index column(s)"""
    index_name: str
    """Name of the index"""

    columns: list[Column]
    """The column(s) to index"""

    is_unique: bool = False
    """True if the index should enforce uniqueness. Equivalent UNIQUE in SQL"""
