from diplomatik.data_model.aggregation.aggregation import Aggregation, AggregationType
from diplomatik.data_model.query.field import Field


class SelectAggregation(Aggregation):
    """
    This aggregation directly selects the field and is used in a group by operation
    """
    distinct: bool = False
    """True to apply a distinct operation on the aggregation. Equivalent to SELECT DISTINCT for SQL"""

    def __init__(self, field: Field, result_alias: str = None, **data):
        super().__init__(command_type=AggregationType.select, field=field, result_alias=result_alias, **data)

