from sqlalchemy import text

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder_factory import \
    QueryBuilderFactory
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    QUERY_PARAM_PLACEHOLDER
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_executors.connection_managers.postgres_connection_manager import \
    PostgresConnectionManager
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_executors.data_source_executor import \
    DataSourceExecutor
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_executors.query_executor_utils import \
    get_query_param_name
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_executors.query_result_adapters.query_result_adapter_factory import \
    QueryResultAdapterFactory
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.query import Query, QueryType
from diplomatik.data_model.query.query_results.query_result import QueryResult, QueryResultType
from diplomatik.data_model.query.query_statement import QueryStatement

DEFAULT_RESULT_TYPE = QueryResultType.py_dict


class PostgresDataSourceExecutor(DataSourceExecutor):
    def execute_read_query(self, query: Query) -> [QueryResult]:
        with PostgresConnectionManager().get_connection() as connection:
            query_type = QueryType.get_by_value(query.query_type)

            statements = QueryBuilderFactory.construct(query_type, DataSourceType.postgres, query).build()

            adapter = QueryResultAdapterFactory.construct(query.data_source_config.source_type,
                                                          self.__get_adapter_type(query))

            query_results = []

            for statement in statements:
                params = self.__get_query_params(statement)

                result = connection.execute(text(statement.expression), params)

                query_results.append(adapter.parse(result))

            return query_results

    def execute_write_query(self, query: Query):
        with PostgresConnectionManager().get_connection() as connection:
            query_type = QueryType.get_by_value(query.query_type)

            statements = QueryBuilderFactory.construct(query_type, DataSourceType.postgres, query).build()

            for statement in statements:
                params = self.__get_query_params(statement)

                connection.execute(text(statement.expression), params)

            connection.commit()

    def __get_adapter_type(self, query: Query) -> QueryResultType:
        if query.query_result_config:
            return query.query_result_config.result_type

        return DEFAULT_RESULT_TYPE

    def __get_query_params(self, statement: QueryStatement) -> dict | list[dict]:
        """
        Replaces the placeholders in the query with the actual values. Since we used named params, the params are
        uniquely named and the order in which it's declared is important.
        Gets the params collection to use in the query execution. For a list of param dicts, it is used where a param
        can represent multiple values, like in an insert query inserting multiple rows.

        :param: the statement to replace for
        :return: the params collection
        """
        for i, param in enumerate(statement.params):
            param_key = get_query_param_name(i)

            statement.expression = statement.expression.replace(QUERY_PARAM_PLACEHOLDER, f":{param_key}", 1)

            param.key = param_key

        return self.__get_bulk_params_list(statement) if statement.is_bulk_params else self.__get_params_dict(statement)

    def __get_params_dict(self, statement: QueryStatement) -> dict:
        return {param.key: param.value for param in statement.params}

    def __get_bulk_params_list(self, statement: QueryStatement) -> list[dict]:
        bulk_params = []

        row_count = len(statement.params[0].value)

        for i in range(row_count):
            bulk_params.append({param.key: param.value[i] for param in statement.params})

        return bulk_params
