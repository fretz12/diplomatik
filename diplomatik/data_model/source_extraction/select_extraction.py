from diplomatik.data_model.query.field import Field
from diplomatik.data_model.source_extraction.limit_offset import LimitOffset
from diplomatik.data_model.source_extraction.order_by import OrderBy
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction, SourceExtractionType
from diplomatik.data_model.source_formation.source_formation import SourceFormation


class SelectExtraction(SourceExtraction):
    """
    The selection source extraction, equivalent to a SQL select statement
    """
    source_formation: SourceFormation
    """The formed source from which to perform the selection on"""

    fields: [Field] = None
    """The fields to select. No need to define if select_all_columns is set"""

    select_all_columns: bool = False
    """True select all columns. Equivalent to SELECT * in SQL"""

    pagination: LimitOffset | None = None
    """Pagination of the selection results"""

    order_by: [OrderBy] = None
    """Orders the results according to the order by definitions, sorted in the order they are defined. Equivalent to 
    ORDER BY in SQL"""

    distinct: bool = False
    """True to return distinct results. Equivalent to SELECT DISTINCT in SQL"""

    def __init__(self, **data):
        super().__init__(extraction_type=SourceExtractionType.select, **data)
