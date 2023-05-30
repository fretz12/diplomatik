from enum import Enum

from pydantic import BaseModel


class MaterializationType(Enum):
    """
    The type of materialization on the query results
    """
    table = 'table'
    """Materialize the data as a new table"""

    temporary_table = 'temporary_table'
    """Materialize the data as as a temporary table"""

    view = 'view'
    """Materialize the data as as a view. View definition is dependent on data source type."""


class MaterializedResult(BaseModel):
    """
    Materialization refers to converting the extracted data into a temporary, logical or persistent data store
    """
    materialization_type: MaterializationType
    """The type of materialization"""

    name: str
    """The name of the materialized result"""
