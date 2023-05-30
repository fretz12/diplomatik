from enum import Enum


from diplomatik.data_engine.data_engine_api.query_component import QueryComponent
from diplomatik.data_model.query.field import Field
from diplomatik.exceptions.exceptions import DataModelException


class AggregationType(Enum):
    """The type of aggregation operation"""

    sum = 'sum'
    """Aggregate a column by summing them up the row values"""

    count = 'count'
    """Aggregate a column by counting the number of rows"""

    average = 'average'
    """Aggregate a column by averaging the row values"""

    min = 'min'
    """Aggregate a column by returning the minimum row value"""

    max = 'max'
    """Aggregate a column by returning the max row value"""

    select = 'select'
    """Aggregate a column by returning the max row value"""

    @classmethod
    def get_by_value(cls, value: str):
        """
        Gets the aggregation type based on its string value

        :param value: the value to match
        :return: the aggregation type
        """
        for agg_type in AggregationType:
            if agg_type.value == value:
                return agg_type

        raise DataModelException(f"{value} is not a valid aggregation type")


class Aggregation(QueryComponent):
    """Definition on how to apply aggregation on a field"""
    aggregation_type: AggregationType
    """The type of aggregation"""

    field: Field | None = None
    """The field to apply the aggregation on"""

    result_alias: str
    """The alias for the aggregated result"""
