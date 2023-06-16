from diplomatik.data_model.query_component import QueryComponent
from diplomatik.data_model.filter.filter import Filter
from diplomatik.data_model.query.field import Field
from diplomatik.data_model.query.functions.function import Function, FunctionCategory, FunctionType


class CaseWhenClause(QueryComponent):
    """
    The clause for a case-when function, equivalent to WHEN condition THEN result in SQL
    """
    condition: Filter
    """The condition to check if true"""

    result: Field
    """The result to return if the condition is true"""


class CaseWhenFunction(Function):
    """
    The function that wraps a "switch-case" around a set of conditions. This is equivalent to CASE WHEN in SQL.
    """
    clauses: list[CaseWhenClause]
    """The clauses to check for a condition and return a result if matched"""

    default_result: Field
    """The result to return if no clauses match"""

    def __init__(self, alias: str = None, **data):
        super().__init__(function_category=FunctionCategory.logic, function_type=FunctionType.case_when,
                         alias=alias, **data)
