from diplomatik.data_engine.data_engine_api.query_component import QueryComponent


class Table(QueryComponent):
    """
    Represents a table in the data source
    """
    table_name: str = ''
    """Name of the table"""

    table_alias: str | None = None
    """Alias of the table"""
