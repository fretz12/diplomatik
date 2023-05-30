from diplomatik.data_model.aggregation.aggregation import Aggregation, AggregationType
from diplomatik.data_model.query.field import Field


class MinAggregation(Aggregation):
    """
    This aggregation gets the minimum value of the field, and is used in group by operations
    """
    def __init__(self, field: Field, result_alias: str = None, **data):
        super().__init__(command_type=AggregationType.min, field=field, result_alias=result_alias, **data)

