from typing import Annotated

from pydantic import Field

from diplomatik.data_model.table_management.add_column_indexes_command import AddColumnIndexesCommand
from diplomatik.data_model.table_management.create_table_command import CreateTableCommand

DataSourceManagementCommandUnion = Annotated[CreateTableCommand | AddColumnIndexesCommand, Field(discriminator='command_type')]
"""The declared datatype that is used in Pydantic models so it knows how to (de)serialize abstract data source 
management command types"""
