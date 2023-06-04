from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.filter.bound_filter import BoundFilter
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.exceptions.exceptions import DataEngineException


class DefaultBoundFilterCompiler(QueryComponentCompiler[BoundFilter]):
    def __init__(self, syntax_policy: SyntaxPolicy, query_component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.query_component_compiler = query_component_compiler

    def compile(self, filter: BoundFilter) -> QueryStatement:
        statement = QueryStatement(expression='', params=[])

        lower_operand, upper_operand = self.__decode_compare_operand(filter)

        field_statement = self.query_component_compiler.compile(filter.field)
        lower_statement = self.query_component_compiler.compile(filter.lower) if filter.lower else None
        upper_statement = self.query_component_compiler.compile(filter.upper) if filter.upper else None

        if filter.lower and filter.upper:
            self.__fill_between_clause(statement, field_statement, lower_statement, upper_statement, lower_operand,
                                       upper_operand)
        elif filter.lower:
            self.__fill_compare_statement(statement, field_statement, lower_statement, lower_operand)
        elif filter.upper:
            self.__fill_compare_statement(statement, field_statement, upper_statement, upper_operand)
        else:
            raise DataEngineException("Invalid bound filter configuration")

        return statement

    def __decode_compare_operand(self, filter: BoundFilter):
        if filter.lower_strict and filter.upper_strict:
            return '>', '<'
        elif filter.lower_strict:
            return '>', '<='
        elif filter.upper_strict:
            return '>=', '<'
        else:
            return '>=', '<='

    def __fill_between_clause(self, statement: QueryStatement,
                              field_statement: QueryStatement,
                              lower_statement: QueryStatement,
                              upper_statement: QueryStatement,
                              lower_operand: str,
                              upper_operand: str):
        expression = \
            f"({field_statement.expression} {lower_operand} {lower_statement.expression} " \
            f"AND " \
            f"{field_statement.expression} {upper_operand} {upper_statement.expression})"

        statement.extend_params(field_statement.params)
        statement.extend_params(lower_statement.params)
        statement.extend_params(upper_statement.params)

        statement.expression += expression

    def __fill_compare_statement(self, statement: QueryStatement, field_statement: QueryStatement,
                                 compare_statement: QueryStatement, compare_operand: str):
        expression = \
            f"({field_statement.expression} {compare_operand} {compare_statement.expression})"

        statement.extend_params(field_statement.params)
        statement.extend_params(compare_statement.params)

        statement.expression += expression
