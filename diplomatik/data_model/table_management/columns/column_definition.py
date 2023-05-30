from enum import Enum

from pydantic import BaseModel

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

    data_type: FieldDataType
    """The data type of the column"""

    extra_definitions: str | None = None,
    """Optional data source specific definitions to add after the data type is declared. It can be any arbitrary 
    string. For example, primary key definition."""

    column_position: ColumnPosition | None = None,
    """The option to order a column based on its relative position to another column"""

    column_order_index: int | None = None
    """The option to order a column based on its order index in the table. Mutually exclusive option from 
    column_position"""
