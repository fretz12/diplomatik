from abc import ABC
from enum import Enum

from pydantic import BaseModel

from diplomatik.exceptions.exceptions import DataModelException


class DataSourceManagementCommandType(Enum):
    """The collection of data source management command types"""
    add_columns = 'add_columns'
    delete_columns = 'delete_columns'
    add_column_indexes = 'add_column_indexes'
    delete_column_indexes = 'delete_column_indexes'
    list_columns = 'list_columns'
    create_table = 'create_table'
    create_table_like = 'create_table_like'
    delete_table = 'delete_table'
    table_exists = 'table_exists'
    alter_table_freeform = 'alter_table_freeform'
    rearrange_columns = 'rearrange_columns'
    create_database = 'create_database'
    create_user = 'create_user'
    grant_all_database_privileges = 'grant_all_database_privileges'
    rename_table = 'rename_table'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the data source management command type based on its string value

        :param value: the value to match
        :return: the aggregation type
        """
        for type in DataSourceManagementCommandType:
            if type.value == value:
                return type

        raise DataModelException("Invalid table management type")


class DataSourceManagementCommand(BaseModel, ABC):
    """The data source management command base model"""
    command_type: DataSourceManagementCommandType
    """The command type"""

