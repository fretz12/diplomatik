from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.source_formation.join_formation import JoinFormation, RightJoinTable


class JoinFormationCompiler(QueryComponentCompiler[JoinFormation]):
    def __init__(self, syntax_policy: SyntaxPolicy, component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.component_compiler = component_compiler

        ## Required for circular import issues
        from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.filter_compilers.default_filter_compiler import \
            DefaultFilterComponentCompiler
        self.filter_compiler = DefaultFilterComponentCompiler(self.syntax_policy, self.component_compiler)

    def compile(self, join_formation: JoinFormation) -> QueryStatement:
        left_table_expression = self.component_compiler.compile(join_formation.left_table).expression

        right_tables_statement = self.__create_right_tables_statement(join_formation)

        return QueryStatement(expression=f"{left_table_expression} {right_tables_statement.expression}",
                              params=right_tables_statement.params)

    def __create_right_tables_statement(self, join_formation: JoinFormation) -> QueryStatement:
        statement = QueryStatement(expression='', params=[])

        join_clauses = []

        for right_table in join_formation.right_tables:
            join_expression = self.__build_join_expression(right_table)
            on_condition_statement = self.filter_compiler.compile(right_table.on_condition)

            join_clause = f"{join_expression} ON {on_condition_statement.expression}"
            join_clauses.append(join_clause)

            statement.extend_params(on_condition_statement.params)

        statement.expression = ' '.join(join_clauses)

        return statement

    def __build_join_expression(self, right_table: RightJoinTable):
        join_type = right_table.join_type.value

        right_table_name = self.component_compiler.compile(right_table.table).expression

        return f"{join_type} JOIN {right_table_name} "
