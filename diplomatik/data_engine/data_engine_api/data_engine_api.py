from abc import ABC, abstractmethod

from diplomatik.data_model.query.query import Query
from diplomatik.data_model.query.query_results.query_result import QueryResult


class DataEngineAPI(ABC):
    @abstractmethod
    def execute_read_query(self, query: Query) -> QueryResult:
        """
        Executes a single read query and returns the results of the execution

        :param query: the query to execute
        :return: the query's results
        """
        pass
