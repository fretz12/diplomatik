from diplomatik.data_model.query_component import QueryComponent, QueryComponentType


class Table(QueryComponent):
    """
    Represents a table in the data source
    """
    table_name: str = ''
    """Name of the table"""

    table_alias: str | None = None
    """Alias of the table"""

    def __init__(self, **data):
        super().__init__(component_type=QueryComponentType.table, **data)
