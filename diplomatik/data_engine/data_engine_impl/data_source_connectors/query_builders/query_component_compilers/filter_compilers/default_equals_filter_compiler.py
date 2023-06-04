from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.filter.equals_filter import EqualsFilter
from diplomatik.data_model.query.query_statement import QueryStatement


class DefaultEqualsFilterCompiler(QueryComponentCompiler[EqualsFilter]):
    def __init__(self, syntax_policy: SyntaxPolicy, query_component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.query_component_compiler = query_component_compiler

    def compile(self, filter: EqualsFilter) -> QueryStatement:
        statement = QueryStatement(expression='', params=[])

        lhs_statement = self.query_component_compiler.compile(filter.lhs)
        statement.extend_params(lhs_statement.params)

        rhs_statement = self.query_component_compiler.compile(filter.rhs)
        statement.extend_params(rhs_statement.params)

        operator = '<>' if filter.negate else '='
        expression = f"({lhs_statement.expression} {operator} {rhs_statement.expression})"

        statement.expression += expression

        return statement
