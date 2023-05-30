from abc import ABC, abstractmethod
from typing import Optional, List

from diplomatik.data_engine.data_engine_api.query_component import QueryComponent
from diplomatik.data_model.filter.filter import FilterType
from diplomatik.data_model.query.functions.function import FunctionCategory
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.table_management.add_column_indexes_command import AddColumnIndexesCommand
from diplomatik.data_model.table_management.add_columns_command import AddColumnsCommand
from diplomatik.data_model.table_management.create_database_command import CreateDatabaseCommand
from diplomatik.data_model.table_management.create_table_command import CreateTableCommand
from diplomatik.data_model.table_management.create_table_like_command import CreateTableLikeCommand
from diplomatik.data_model.table_management.delete_column_indexes_command import DeleteColumnIndexesCommand
from diplomatik.data_model.table_management.delete_table_command import DeleteTableCommand
from diplomatik.data_model.table_management.list_columns_command import ListColumnsCommand
from diplomatik.data_model.table_management.rename_table_command import RenameTableCommand
from diplomatik.data_model.table_management.table_exists_command import TableExistsCommand


class DataSourceConnector(ABC):
    @abstractmethod
    def compile_query_component(self, query_component: QueryComponent) -> QueryStatement:
        """
        Takes in a query component and builds it into an executable query statement

        :param query_component: the query component to build on
        :return: the query statement
        """
        pass

    @abstractmethod
    def execute_read_query(self, statement: QueryStatement):
        """
        Executes the query on the give data source

        :param statement: the statement to execute
        :return: results of the query
        """
        pass

    @abstractmethod
    def execute_transaction(self, statements: [QueryStatement], execute_as_transaction: bool = True):
        """
        Executes the provided statements in order as a transaction. Any errors should be rolled back.

        :param statements: the statements to execute
        the master data source
        :return the results, if any
        """
        pass

    # @abstractmethod
    # def write_from_dataframe(self, df: DataFrame, config: DataFrameToSqlConfig, user_id: Optional[int] = None):
    #     """
    #     Takes a Pandas dataframe and writes it directly into the data source. This is a pass through of Pandas's to_sql
    #     method
    #
    #     :param df: the dataframe to write from
    #     :param config: the data frame to data source configs
    #     :param user_id: ID of the user to write for. If provided, targets the user tables data source, else targets
    #     the master data source
    #     """
    #     pass
    #
    # @abstractmethod
    # def read_to_dataframe(self, config: DataFrameFromSqlConfig, user_id: Optional[int] = None) -> DataFrame:
    #     """
    #     Takes a query and executes it with the results put directly into a pandas dataframe. This is a pass through of
    #     Panda's read_sql_query API
    #
    #     :param config: config for the execution
    #     :param user_id: user to read for
    #     :return: the returned dataframe
    #     """
    #     pass

    @abstractmethod
    def flush_session(self):
        """
        Flushes/commits any changes in the ORM session so that all the data is coherent
        """
        pass

    @abstractmethod
    def init_statement_params_collection(self, *values):
        """
        Initializes the collection to prepared statement params. The collection type can be connector specific. For
        example, SQLAlchemy 1.3 uses arrays

        :param values: the values to initialize the collection with, if provided
        :return: the initialized collection
        """
        pass

    @abstractmethod
    def parametrize_expression_value(self, value=None):
        """
        Turns the provided value into a parametrized value for a prepared statement.

        :param value: the value to parametrize
        :return: the parametrized value
        """
        pass

    @abstractmethod
    def extend_params_collection(self, sub_collection, param_collection):
        """
        Concats the parametrized values collection. The collection type is connector specific.

        :param sub_collection: the sub collection to append
        :param param_collection: the main collection to extend from
        :return: the combined collection
        """
        pass

    @abstractmethod
    def escape_sql_keyword(self, keyword: str):
        """
        Wraps the SQL keyword with database specific characters to they are escaped

        :param keyword: the keyword to wrap
        :return: the escaped keyword
        """
        pass

    @abstractmethod
    def to_sql_string_literal(self, param: str) -> str:
        """
        Converts the provided arg into a string literal that is specific to the database

        :param param: the param to convert
        :return: the string literal
        """
        pass

    @abstractmethod
    def is_filter_connector_specific(self, filter_type: FilterType) -> bool:
        """
        :param filter_type: the type of filter to check
        :return: True if the filter's implementation is defined by the connector
        """
        pass

    @abstractmethod
    def get_filter_statement(self, filter_type: FilterType, **kwargs) -> QueryStatement:
        """
        Gets the filter's compiled query statement

        :param filter_type: the type of filter to get for
        :param kwargs: optional args for the filter
        :return: the filter's statement
        """
        pass

    @abstractmethod
    def create_add_table_columns_statement(self, command: AddColumnsCommand, user_id: Optional[int]) -> QueryStatement:
        """
        Adds columns to a table

        :param command: command containing instructions to add
        :param user_id: the user to add for
        :return: the query statement
        """
        pass

    @abstractmethod
    def create_add_source_table_columns_statement(self, command, user_id: Optional[int]) -> QueryStatement:
        """
        Creates the statement to add columns to a source table

        :param command: command containing instructions to add
        :type AddSourceTableColumnsCommand
        :param user_id: the user to add for
        :return: the query statement
        """
        pass

    @abstractmethod
    def create_delete_table_columns_statement(self, command) -> QueryStatement:
        """
        Deletes columns in a table

        :param command: command containing instructions to delete
        :type DeleteColumnsCommand
        :return: the query statement
        """
        pass

    @abstractmethod
    def create_add_table_indexes_statement(self, command: AddColumnIndexesCommand, user_id: Optional[int]) \
            -> Optional[QueryStatement]:
        """
        Index columns in a table

        :param command: command containing instructions to index
        :param user_id the user to create for
        :return: the query statement, or None if all indexes already exist in the table columns
        """
        pass

    @abstractmethod
    def create_delete_table_indexes_statement(self, command: DeleteColumnIndexesCommand, user_id: Optional[int]) \
            -> Optional[QueryStatement]:
        """
        Deletes column indexes in a table

        :param command: command containing instructions to delete
        :param user_id: the user to create for
        :return: the query statement
        """
        pass

    @abstractmethod
    def create_list_table_columns_statement(self, command: ListColumnsCommand) -> QueryStatement:
        """
        Lists all columns of a table

        :param command: command containing instructions to list
        :return: the query statement
        """
        pass

    @abstractmethod
    def create_add_table_statement(self, command: CreateTableCommand) -> QueryStatement:
        """
        Creates a table. If the table already exists it will error out.

        :param command: command containing instructions to create
        :return: the query statement
        """
        pass

    @abstractmethod
    def create_add_table_like_statement(self, command: CreateTableLikeCommand) -> QueryStatement:
        """
        Creates the statement ot create a table like another table, preserving the schema and indexes

        :param command: command containing instructions to create
        :return: the query statement
        """
        pass


    @abstractmethod
    def create_delete_table_statement(self, command: DeleteTableCommand) -> QueryStatement:
        """
        Deletes a table

        :param command: command containing instructions to delete
        :return: the query statement
        """
        pass

    @abstractmethod
    def create_table_exists_statement(self, command: TableExistsCommand) -> QueryStatement:
        """
        Creates the statement to check if a table exists

        :param command: command containing the table name
        :return: the query statement
        """
        pass

    @abstractmethod
    def create_alter_table_freeform_statement(self, command) -> QueryStatement:
        """
        Executes a generic alter table freeform command

        :param command: command containing instructions to alter
        :type AlterTableFreeformCommand
        :return: the query statement
        """
        pass


    @abstractmethod
    def create_database_statement(self, command: CreateDatabaseCommand) -> QueryStatement:
        """
        Creates the statement to create a new database

        :param command: command containing the instructions to create a new database
        :return: the query statement
        """
        pass


    @abstractmethod
    def create_rename_table_statement(self, command: RenameTableCommand) -> QueryStatement:
        """
        Renames a table

        :param command: the command containing the instructions to rename
        :return: the query statement
        """
        pass

    @abstractmethod
    def get_function_definitions(self, categories: [FunctionCategory] = None) -> List[dict]:
        """
        Gets the list of function definitions

        :param categories: the categories to get functions for. If not provided, all categories will be returned
        :return: the list of functions
        """
        pass
