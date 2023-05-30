from abc import ABC
from enum import Enum

from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig
from diplomatik.data_model.query.table import Table
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction


class InsertType(Enum):
    values = 'values'
    selection = 'selection'


class InsertQuery(Query, ABC):
    """Base class for an insert query"""
    insert_type: InsertType
    """The insert type"""

    table: Table
    """The table to insert into"""

    columns: [Column]
    """The columns to insert data into"""

    def __init__(self, data_source_config: DataSourceConfig,
                 query_result_config: QueryResultConfig = None,
                 query_id: str | None = None,
                 event_hooks: [EventHook] = None,
                 **data):
        super().__init__(query_type=QueryType.insert,
                         data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)


class InsertValuesQuery(InsertQuery):
    """
    Query to insert values
    """
    values: [[str]]
    """the values to insert"""

    on_duplicate_key: bool = False
    """If one or more of the columns is a unique key, the existing row will be updated. If the key doesn't exist, then 
    insert the values. This is supported only on certain data sources"""

    def __init__(self, table: Table,
                 columns: [Column],
                 data_source_config: DataSourceConfig,
                 query_result_config: QueryResultConfig = None,
                 query_id: str | None = None,
                 event_hooks: [EventHook] = None,
                 **data):
        super().__init__(insert_type=InsertType.values,
                         table=table,
                         columns=columns,
                         data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)


class InsertSelectionQuery(InsertQuery):
    """
    Query to insert values into a table based on a selection's output
    """
    source_extraction: SourceExtraction
    """Definition on how data is extracted to be inserted"""

    filter: Filter | None = None
    """Optional filter to apply to the extracted data"""

    def __init__(self, table: Table,
                 columns: [Column],
                 data_source_config: DataSourceConfig,
                 query_result_config: QueryResultConfig = None,
                 query_id: str | None = None,
                 event_hooks: [EventHook] = None,
                 **data):
        super().__init__(insert_type=InsertType.selection,
                         table=table,
                         columns=columns,
                         data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)
