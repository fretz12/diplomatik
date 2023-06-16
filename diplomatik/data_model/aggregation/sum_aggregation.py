from diplomatik.data_model.aggregation.aggregation import Aggregation, AggregationType
from diplomatik.data_model.query.field import Field


class SumAggregation(Aggregation):
    """
    This aggregation sums the field, and is used in group by operations
    """
    def __init__(self, field: Field, result_alias: str = None, **data):
        super().__init__(command_type=AggregationType.average, field=field, result_alias=result_alias, **data)
