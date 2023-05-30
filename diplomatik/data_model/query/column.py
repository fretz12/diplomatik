from diplomatik.data_engine.data_engine_api.query_component import QueryComponentType
from diplomatik.data_model.query.field import Field, FieldDataType


class Column(Field):
    """
    The column field that directly refers to a data source's table's column
    """
    column_name: str
    """Name of the column"""

    table_name: str | None = None
    """Name of the table the column belongs to. Required if a query references multiple tables so there is no 
    ambiguity"""

    def __init__(self, data_type: FieldDataType | None = None, alias: str | None = None, **data):
        super().__init__(component_type=QueryComponentType.column, data_type=data_type, alias=alias, **data)
