from sqlalchemy import text, bindparam

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
                self.__replace_query_params(statement)

                bind_params = [bindparam(key=param.key, value=param.value) for param in statement.params]

                bound_query = text(statement.expression).bindparams(*bind_params)

                result = connection.execute(bound_query)

                query_results.append(adapter.parse(result))

            return query_results

    def execute_write_query(self, query: Query):
        with PostgresConnectionManager().get_connection() as connection:
            query_type = QueryType.get_by_value(query.query_type)

            statements = QueryBuilderFactory.construct(query_type, DataSourceType.postgres, query).build()

            for statement in statements:
                self.__replace_query_params(statement)

                bind_params = [bindparam(key=param.key, value=param.value) for param in statement.params]

                bound_query = text(statement.expression).bindparams(*bind_params)

                connection.execute(bound_query)

            connection.commit()

    def __get_adapter_type(self, query: Query) -> QueryResultType:
        if query.query_result_config:
            return query.query_result_config.result_type

        return DEFAULT_RESULT_TYPE

    def __replace_query_params(self, statement: QueryStatement):
        """
        Replaces the placeholders in the query with the actual values. Since we used named params, the params are
        uniquely named and the order in which it's declared is important

        :param statement: the statement to replace for
        """
        for i, param in enumerate(statement.params):
            param_key = get_query_param_name(i)

            statement.expression = statement.expression.replace(QUERY_PARAM_PLACEHOLDER, f":{param_key}", 1)

            param.key = param_key
