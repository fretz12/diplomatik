from diplomatik.data_model.query.field import FieldDataType
from diplomatik.data_model.table_management.columns.column_definition import ColumnPosition, CreateColumnDefinition


class CreateStringColumnDefinition(CreateColumnDefinition):
    """
    Definition for creating a string column
    """
    byte_count: int
    """Number of bytes in the string. Equivalent to VARCHAR in SQL."""

    def __init__(self, column_name: str,  column_position: ColumnPosition = None, column_order_index: int = None,
                 **data):
        super().__init__(column_name=column_name, data_type=FieldDataType.string, column_position=column_position,
                         column_order_index=column_order_index, **data)
