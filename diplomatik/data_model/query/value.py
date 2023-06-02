import re
from typing import Literal

from diplomatik.data_model.query_component import QueryComponentType
from diplomatik.data_model.query.field import Field, FieldDataType, FieldType

FIELD_PLACEHOLDER = '__field_placeholder__'


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

    fields: list | None = None
    """The list of fields to fill the placeholders in the expression"""

    def __init__(self, data_type: FieldDataType | None = None, alias: str | None = None, **data):
        super().__init__(component_type=QueryComponentType.value, data_type=data_type, alias=alias, **data)
