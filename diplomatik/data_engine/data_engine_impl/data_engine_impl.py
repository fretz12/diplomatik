from diplomatik.data_engine.data_engine_api.data_engine_api import DataEngineAPI
from diplomatik.data_engine.data_engine_impl.data_source_connectors.data_source_executor_factory import \
    DataSourceExecutorFactory
from diplomatik.data_model.query.query import Query
from diplomatik.data_model.query.query_results.query_result import QueryResult
from diplomatik.exceptions.exceptions import DataEngineException


class DataEngineImpl(DataEngineAPI):
    def execute_read_query(self, query: Query) -> QueryResult:
        if not query.data_source_config:
            raise DataEngineException("Missing data source config")

        executor = DataSourceExecutorFactory.construct(query.data_source_config.source_type)

        return executor.execute_read_query(query)

    def execute_write_query(self, query: Query):
        if not query.data_source_config:
            raise DataEngineException("Missing data source config")

        executor = DataSourceExecutorFactory.construct(query.data_source_config.source_type)

        executor.execute_write_query(query)
