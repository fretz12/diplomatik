from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.query_component import QueryComponent


T = TypeVar("T", bound=QueryComponent)


class QueryComponentCompiler(ABC, Generic[T]):
    """
    The base class for query component compilers
    """
    @abstractmethod
    def compile(self, component: T) -> QueryStatement:
        """
        Takes a query component and turns it into a query statement

        :param component: the component to build for
        :return: the query statement
        """
        pass
