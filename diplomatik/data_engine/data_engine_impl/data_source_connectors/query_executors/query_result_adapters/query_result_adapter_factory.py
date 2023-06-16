
from pydantic import BaseModel

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_executors.query_result_adapters.sqlalchemy_pydict_adapter import \
    SqlAlchemyPydictAdapter
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.query_results.query_result import QueryResultType
from diplomatik.exceptions.exceptions import DataEngineException


class QueryResultAdapterFactory(BaseModel):
    """
    Factory for creating query result adapters
    """
    @staticmethod
    def construct(source_type: DataSourceType, result_type: QueryResultType):
        """
        Fetches the query result adapter based on the source type and result type

        :param source_type: the source type to match
        :param result_type: the result type to match
        :return: the query result adapter
        """
        adapters = {
            (DataSourceType.postgres, QueryResultType.py_dict): SqlAlchemyPydictAdapter,
        }

        if (source_type, result_type) not in adapters:
            raise DataEngineException(f"Unsupported data source type: {source_type} and result type: {result_type}")

        return adapters[(source_type, result_type)]()
