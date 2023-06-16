from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.filter.null_check_filter import NullCheckFilter
from diplomatik.data_model.query.query_statement import QueryStatement


class DefaultNullCheckFilterCompiler(QueryComponentCompiler[NullCheckFilter]):
    def __init__(self, syntax_policy: SyntaxPolicy, query_component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.query_component_compiler = query_component_compiler

    def compile(self, filter: NullCheckFilter) -> QueryStatement:
        statement = QueryStatement(expression='', params=[])

        field_statement = self.query_component_compiler.compile(filter.field)
        statement.extend_params(field_statement.params)

        null_expression = 'IS NOT NULL' if filter.negate else 'IS NULL'

        empty_as_null_expression = self.__get_empty_as_null_expression(filter, field_statement)

        expression = f"({field_statement.expression} {null_expression}{empty_as_null_expression})"

        statement.expression += expression

        return statement

    def __get_empty_as_null_expression(self, filter: NullCheckFilter, field_statement: QueryStatement):
        if not filter.empty_as_null:
            return ''

        operator = '<>' if filter.negate else '='

        return f" OR {field_statement.expression} {operator} ''"
