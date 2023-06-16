from enum import Enum

from pydantic import BaseModel


class DataFrameToSqlIfExistsPolicy(Enum):
    replace = "replace"
    append = "append"
    fail = "fail"


class DataFrameToSqlConfig(BaseModel):
    """
    This is a direct passthrough for the params in the pandas dataframe to_sql API. Some params are not exposed as
    they are determined by the engine. See:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
    """
    table_name: str
    if_exists_policy: DataFrameToSqlIfExistsPolicy = DataFrameToSqlIfExistsPolicy.fail
    data_types: dict = None


class DataFrameFromSqlConfig(BaseModel):
    """
    This is a direct passthrough for the params in the pandas dataframe read_sql_query API. Some params are not exposed
    as they are determined by the engine. See:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql_query.html
    """
    query: str
    params: list = None
