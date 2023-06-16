from enum import Enum

from diplomatik.exceptions.exceptions import DataModelException


class DataSourceType(Enum):
    """
    The data source types
    """
    postgres = 'postgres'

    @classmethod
    def get_by_value(cls, value: str):
        """
        Gets the data source type based on its string value

        :param value: the value to match
        :return: the data source type
        """
        for source in DataSourceType:
            if source.value == value:
                return source

        raise DataModelException(f"{value} is not a valid data source type")
