from typing import Literal

from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.field_union_type import FieldUnion
from diplomatik.data_model.source_extraction.limit_offset import LimitOffset
from diplomatik.data_model.source_extraction.order_by import OrderByMultiple
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction, SourceExtractionType
from diplomatik.data_model.source_formation.source_formation_union_type import SourceFormationUnion


class SelectExtraction(SourceExtraction):
    """
    The selection source extraction, equivalent to a SQL select statement
    """
    extraction_type: Literal[SourceExtractionType.select.value]
    """The type of source extraction"""

    source_formation: SourceFormationUnion
    """The formed source from which to perform the selection on"""

    fields: list[FieldUnion] | None = None
    """The fields to select. No need to define if select_all_columns is set"""

    select_all_columns: bool = False
    """True select all columns. Equivalent to SELECT * in SQL"""

    pagination: LimitOffset | None = None
    """Pagination of the selection results"""

    distinct: bool = False
    """True to return distinct results. Equivalent to SELECT DISTINCT in SQL"""

    def __init__(self, filter: Filter | None = None, order_by: OrderByMultiple | None = None, **data):
        super().__init__(filter=filter, order_by=order_by, **data)
