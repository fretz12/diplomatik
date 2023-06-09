from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy, QUERY_PARAM_PLACEHOLDER
from diplomatik.data_model.filter.like_filter import LikeFilter
from diplomatik.data_model.query.query_statement import QueryStatement, QueryParam


class DefaultLikeFilterCompiler(QueryComponentCompiler[LikeFilter]):
    def __init__(self, syntax_policy: SyntaxPolicy, query_component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.query_component_compiler = query_component_compiler

    def compile(self, filter: LikeFilter) -> QueryStatement:
        statement = QueryStatement(expression='', params=[])

        field_statement = self.query_component_compiler.compile(filter.field)
        statement.extend_params(field_statement.params)

        like_expression = 'NOT LIKE' if filter.negate else 'LIKE'

        expression = f"({field_statement.expression} {like_expression} {QUERY_PARAM_PLACEHOLDER})"
        statement.extend_params([QueryParam(value=filter.matcher)])

        statement.expression += expression

        return statement
