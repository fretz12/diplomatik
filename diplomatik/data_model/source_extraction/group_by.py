from diplomatik.data_engine.data_engine_api.query_component import QueryComponent
from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.field import Field


class GroupBy(QueryComponent):
    """
    Query definition for the GROUP BY operation of SQL
    """
    fields: [Field]
    """The fields to perform the group by on"""

    having: Filter | None = None
    """Filters the results after the group by is performed. Equivalent to HAVING in SQL"""
