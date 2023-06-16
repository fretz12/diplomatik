from diplomatik.data_engine.data_engine_api.data_engine_api import DataEngineAPI
from diplomatik.data_engine.data_engine_impl.data_engine_impl import DataEngineImpl


class DataEngineFactory:
    @staticmethod
    def create_engine() -> DataEngineAPI:
        """
        Creates the data engine used for executing queries on the data sources
        """
        return DataEngineImpl()
