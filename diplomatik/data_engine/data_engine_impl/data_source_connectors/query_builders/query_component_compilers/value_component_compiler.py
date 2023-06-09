import re

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy, QUERY_PARAM_PLACEHOLDER
from diplomatik.data_model.query.query_statement import QueryStatement, QueryParam
from diplomatik.data_model.query.value import Value, FIELD_PLACEHOLDER


class ValueComponentCompiler(QueryComponentCompiler[Value]):
    def __init__(self, syntax_policy: SyntaxPolicy, query_component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.query_component_compiler = query_component_compiler

    def compile(self, value: Value) -> QueryStatement:
        if value.fields:
            statement = self.__get_compiled_fields_statement(value)
        else:
            statement = self.__get_value_only_statement(value)

        if value.alias:
            statement.expression += f" as {value.alias}"

        return statement

    def __get_compiled_fields_statement(self, value: Value) -> QueryStatement:
        statement = QueryStatement(expression=value.expression, params=[])

        for field in value.fields:
            field_statement = self.query_component_compiler.compile(field)

            statement.expression = statement.expression.replace(FIELD_PLACEHOLDER, field_statement.expression, 1)
            if field_statement.params:
                statement.params.extend(field_statement.params)

        return statement

    def __get_value_only_statement(self, value: Value) -> QueryStatement:
        if not value.expression:
            return QueryStatement(expression='NULL')

        return QueryStatement(expression=QUERY_PARAM_PLACEHOLDER, params=[QueryParam(value=value.expression)])
