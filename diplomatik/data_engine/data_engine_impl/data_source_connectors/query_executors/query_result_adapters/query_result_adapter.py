from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from diplomatik.data_model.query.query_results.query_result import QueryResult

T = TypeVar("T")
R = TypeVar("R", bound=QueryResult)


class QueryResultAdapter(ABC, Generic[T, R]):
    """
    The base query result adapter to convert queried results into their desired format
    """
    @abstractmethod
    def parse(self, query_result: T) -> R:
        """
        Parses the query result and returns data in the specified format

        :param query_result: the query result to parse
        :return: the parsed result in the specified format
        """
        pass
