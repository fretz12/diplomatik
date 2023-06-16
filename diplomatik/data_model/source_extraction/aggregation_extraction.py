from typing import Literal

from diplomatik.data_model.aggregation.aggregation import Aggregation
from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.source_extraction.group_by import GroupBy
from diplomatik.data_model.source_extraction.order_by import OrderByMultiple
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction, SourceExtractionType
from diplomatik.data_model.source_formation.source_formation_union_type import SourceFormationUnion


class AggregationExtraction(SourceExtraction):
    """
    The definition to extract a source via aggregations
    """
    extraction_type: Literal[SourceExtractionType.aggregate.value]
    """The type of source extraction"""

    aggregations: list[Aggregation]
    """The aggregations to apply"""

    source_formation: SourceFormationUnion
    """The formed source from which to perform the aggregation on"""

    group_by: GroupBy | None = None
    """The definition on how to group by, equivalent to GROUP BY in SQL"""

    def __init__(self, filter: Filter | None = None, order_by: OrderByMultiple | None = None, **data):
        super().__init__(filter=filter, order_by=order_by, **data)
