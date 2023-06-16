from typing import Literal, ForwardRef

from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.functions.function import Function
from diplomatik.data_model.query_component import QueryComponentType
from diplomatik.data_model.query.field import Field, FieldDataType

FIELD_PLACEHOLDER = '__field_placeholder__'

Value = ForwardRef('Value')


class Value(Field):
    """
    A flexible method of defining any SQL expression. This can be a literal, formula, or any arbitrary data source
    specific expression that the data source connector knows how to process. Note that if any fields are used in the
    expression, the expression should substitute the fields with __field_placeholder__, which will be replaced later
    with the provided fields in order
    """
    field_type: Literal['value']
    """The type of field"""

    expression: str
    """The arbitrary query expression"""

    fields: list[Column | Function | Value] | None = None
    """The list of fields to fill the placeholders in the expression"""

    def __init__(self, data_type: FieldDataType | None = None, alias: str | None = None, **data):
        super().__init__(component_type=QueryComponentType.value, data_type=data_type, alias=alias, **data)


Value.update_forward_refs()
