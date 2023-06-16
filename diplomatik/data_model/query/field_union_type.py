from typing import Annotated

from pydantic import Field

from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.functions.function import Function
from diplomatik.data_model.query.value import Value

FieldUnion = Annotated[Column | Function | Value, Field(discriminator='field_type')]
"""The declared datatype that is used in Pydantic models so it knows how to (de)serialize abstract Field types"""
