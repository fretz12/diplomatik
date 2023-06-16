from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.source_extraction.limit_offset import LimitOffset


class LimitOffsetCompiler(QueryComponentCompiler[LimitOffset]):
    def __init__(self, syntax_policy: SyntaxPolicy):
        self.syntax_policy = syntax_policy

    def compile(self, limit_offset: LimitOffset) -> QueryStatement:
        offset = '' if limit_offset.offset is None else f" OFFSET {limit_offset.offset}"

        return QueryStatement(expression=f"LIMIT {limit_offset.limit}{offset} ")
