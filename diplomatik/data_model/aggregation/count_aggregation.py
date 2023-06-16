from diplomatik.data_model.aggregation.aggregation import Aggregation, AggregationType
from diplomatik.data_model.query.field import Field


class CountAggregation(Aggregation):
    """
    This aggregation counts the number of rows for a field and is used in a by group by operation
    """
    count_all: bool = False
    """True to include every single row in the count. This is useful when you want to count very single row in a table, 
    including those with null values. Equivalent to COUNT(*) for SQL. Leave field arg as empty if counting all"""
    def __init__(self, result_alias: str, field: Field | None = None, **data):
        super().__init__(command_type=AggregationType.count, field=field, result_alias=result_alias, **data)
