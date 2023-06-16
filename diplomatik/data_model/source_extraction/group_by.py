from diplomatik.data_model.query_component import QueryComponent, QueryComponentType
from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.field import Field


class GroupBy(QueryComponent):
    """
    Query definition for the GROUP BY operation of SQL
    """
    fields: list[Field]
    """The fields to perform the group by on"""

    having: Filter | None = None
    """Filters the results after the group by is performed. Equivalent to HAVING in SQL"""

    def __init__(self, **data):
        super().__init__(component_type=QueryComponentType.group_by, **data)