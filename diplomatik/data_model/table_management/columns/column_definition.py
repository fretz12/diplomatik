from enum import Enum
from typing import Literal, Annotated

from pydantic import BaseModel, Field

from diplomatik.data_model.query.field import FieldDataType
from diplomatik.exceptions.exceptions import DataModelException


class ColumnPositionType(Enum):
    """The positioning of a column relative to another"""
    before = 'before'
    after = 'after'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the column position type based on its string value

        :param value: the value to match
        :return: the column position type
        """
        for type in ColumnPositionType:
            if type.value == value:
                return type

        raise DataModelException("Invalid column position type")


class ColumnPosition(BaseModel):
    """
    The position to put a column within a table
    """
    position_type: ColumnPositionType
    """The column's position type"""

    relative_to_column: str
    """The column's position relative to another column based on the defined position_type"""


class CreateColumnDefinition(BaseModel):
    """
    Information defining a column within a table

    :param column_position: the option to order a column based on its relative position
    :param column_order_index: the option to order a column based on its order index in the table. Mutually
    exclusive option from column_position
    """
    column_name: str
    """Name of the column"""

    extra_definitions: str | None = None,
    """Optional data source specific definitions to add after the data type is declared. It can be any arbitrary 
    string. For example, primary key definition."""

    column_position: ColumnPosition | None = None,
    """The option to order a column based on its relative position to another column"""

    column_order_index: int | None = None
    """The option to order a column based on its order index in the table. Mutually exclusive option from 
    column_position"""


class CreateStringColumnDefinition(CreateColumnDefinition):
    """
    Definition for creating a string column
    """
    data_type: Literal[FieldDataType.string.value]
    """The data type of the column"""

    byte_count: int
    """Number of bytes in the string. Equivalent to VARCHAR in SQL."""

    def __init__(self, column_name: str,
                 column_position: ColumnPosition = None,
                 column_order_index: int = None,
                 extra_definitions: str | None = None,
                 **data):
        super().__init__(column_name=column_name, column_position=column_position, extra_definitions=extra_definitions,
                         column_order_index=column_order_index, **data)


class CreateInt32ColumnDefinition(CreateColumnDefinition):
    """
    Definition for creating an int32 column
    """
    data_type: Literal[FieldDataType.int32.value]
    """The data type of the column"""


class CreateInt64ColumnDefinition(CreateColumnDefinition):
    """
    Definition for creating an int64 column
    """
    data_type: Literal[FieldDataType.int64.value]
    """The data type of the column"""


class CreateFloat32ColumnDefinition(CreateColumnDefinition):
    """
    Definition for creating a float32 column
    """
    data_type: Literal[FieldDataType.float32.value]
    """The data type of the column"""


class CreateFloat64ColumnDefinition(CreateColumnDefinition):
    """
    Definition for creating a float64 column
    """
    data_type: Literal[FieldDataType.float64.value]
    """The data type of the column"""


class CreateDateColumnDefinition(CreateColumnDefinition):
    """
    Definition for creating a date column
    """
    data_type: Literal[FieldDataType.date.value]
    """The data type of the column"""


class CreateAutoIncrementIntColumnDefinition(CreateColumnDefinition):
    """
    Definition for creating an auto_incrementing int column
    """
    data_type: Literal[FieldDataType.auto_increment_int.value]
    """The data type of the column"""


CreateColumnDefinitionUnion = Annotated[CreateStringColumnDefinition |
                                        CreateInt32ColumnDefinition |
                                        CreateInt64ColumnDefinition |
                                        CreateFloat32ColumnDefinition |
                                        CreateFloat64ColumnDefinition |
                                        CreateDateColumnDefinition |
                                        CreateAutoIncrementIntColumnDefinition, Field(discriminator='data_type')]
"""The declared datatype that is used in Pydantic models so it knows how to (de)serialize abstract data source 
management command types"""
