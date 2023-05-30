from diplomatik.data_model.aggregation.aggregation import Aggregation
from diplomatik.data_model.source_extraction.group_by import GroupBy
from diplomatik.data_model.source_extraction.order_by import OrderBy
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction, SourceExtractionType
from diplomatik.data_model.source_formation.source_formation import SourceFormation


class AggregationExtraction(SourceExtraction):
    """
    The definition to extract a source via aggregations
    """
    aggregations: [Aggregation]
    """The aggregations to apply"""
    source_formation: SourceFormation
    """The formed source from which to perform the aggregation on"""
    group_by: GroupBy | None = None
    """The definition on how to group by, equivalent to GROUP BY in SQL"""
    order_by: [OrderBy] = None
    """Orders the results according to the order by definitions, sorted in the order they are defined. Equivalent to 
    ORDER BY in SQL"""

    def __init__(self, **data):
        super().__init__(extraction_type=SourceExtractionType.aggregate, **data)
