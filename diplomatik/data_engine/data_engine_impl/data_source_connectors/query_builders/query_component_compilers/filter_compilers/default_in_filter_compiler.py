from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy, QUERY_PARAM_PLACEHOLDER
from diplomatik.data_model.filter.in_filter import InFilter
from diplomatik.data_model.query.query_statement import QueryStatement, QueryParam


class DefaultInFilterCompiler(QueryComponentCompiler[InFilter]):
    def __init__(self, syntax_policy: SyntaxPolicy, query_component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.query_component_compiler = query_component_compiler

    def compile(self, filter: InFilter) -> QueryStatement:
        statement = QueryStatement(expression='', params=[])

        field_statement = self.query_component_compiler.compile(filter.field)
        statement.extend_params(field_statement.params)

        in_expression = 'NOT IN' if filter.negate else 'IN'

        parametrized_values = [QUERY_PARAM_PLACEHOLDER for _ in filter.in_values]
        values_list = ', '.join(parametrized_values)
        in_values_params = [QueryParam(value=v) for v in filter.in_values]

        expression = f"({field_statement.expression} {in_expression} ({values_list}))"
        statement.extend_params(in_values_params)

        statement.expression += expression

        return statement
