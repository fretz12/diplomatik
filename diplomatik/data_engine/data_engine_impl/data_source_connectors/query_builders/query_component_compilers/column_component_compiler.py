from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.query.column import Column
from diplomatik.data_model.query.query_statement import QueryStatement


class ColumnComponentCompiler(QueryComponentCompiler[Column]):
    def __init__(self, syntax_policy: SyntaxPolicy):
        self.syntax_policy = syntax_policy

    def compile(self, column: Column) -> QueryStatement:
        alias = ''
        if column.alias:
            alias = f" AS {column.alias}"

        column_name = self.syntax_policy.to_sql_identifier(column.column_name) + alias

        if not column.table_name:
            return QueryStatement(expression=column_name)

        return QueryStatement(expression=f"{self.syntax_policy.to_sql_identifier(column.table_name)}."
                                         f"{column_name}")
