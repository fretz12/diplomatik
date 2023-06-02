from abc import ABC, abstractmethod

from diplomatik.data_model.query.query_statement import QueryStatement


class QueryBuilder(ABC):
    """Based class for building query statements"""

    @abstractmethod
    def build(self) -> list[QueryStatement]:
        """
        Builds a query statement

        :return: the query statement
        """
        pass
