from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.query.table import Table


class TableComponentCompiler(QueryComponentCompiler[Table]):
    def __init__(self, syntax_policy: SyntaxPolicy):
        self.syntax_policy = syntax_policy

    def compile(self, table: Table) -> QueryStatement:
        table_name = self.syntax_policy.to_sql_identifier(table.table_name)

        if not table.table_alias:
            return QueryStatement(expression=table_name)

        return QueryStatement(expression=f"{table_name} {self.syntax_policy.to_sql_identifier(table.table_alias)}")
