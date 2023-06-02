from abc import ABC, abstractmethod


QUERY_PARAM_PLACEHOLDER = "__param_placeholder__"


class SyntaxPolicy(ABC):
    """
    Base class for handling any data source related query syntax
    """
    @abstractmethod
    def to_sql_identifier(self, keyword: str):
        """
        Dresses the provided keyword with the source specific syntax, i.e., quotes or backticks

        :param keyword: the keyword to convert
        :return: the converted keyword
        """
        pass

    @abstractmethod
    def to_sql_string_literal(self, param: str) -> str:
        """
        Converts the provided param to a string literal that is data source specific

        :param param: the arg to convert
        :return: the converted string
        """
        pass
