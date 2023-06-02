from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_executors.data_source_executor import \
    DataSourceExecutor
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_executors.postgres.postgres_data_source_executor import \
    PostgresDataSourceExecutor
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.exceptions.exceptions import DataEngineException


class DataSourceExecutorFactory:
    """"
    Factory for creating data source executors
    """

    @staticmethod
    def construct(source_type: DataSourceType) -> DataSourceExecutor:
        """
        Creates a data source executor

        :param source_type: the data source type to get the executor for
        :return: the data source executor
        """
        connectors = {
            DataSourceType.postgres: PostgresDataSourceExecutor
        }

        if source_type not in connectors:
            raise DataEngineException(f"Unknown data source type: {source_type}")

        return connectors[source_type]()
