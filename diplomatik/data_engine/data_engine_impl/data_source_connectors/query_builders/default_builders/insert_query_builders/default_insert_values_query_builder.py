from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder import QueryBuilder
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler_factory import \
    QueryComponentCompilerFactory
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    QUERY_PARAM_PLACEHOLDER
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy_factory import \
    SyntaxPolicyFactory
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.insert_query import InsertValuesQuery
from diplomatik.data_model.query.query_statement import QueryStatement, QueryParam


## TODO Support on duplicate keys
class DefaultInsertValuesQueryBuilder(QueryBuilder):
    def __init__(self, source_type: DataSourceType, query: InsertValuesQuery):
        self.query = query

        syntax_policy = SyntaxPolicyFactory.construct(source_type)
        self.component_compiler = QueryComponentCompilerFactory.construct(source_type, syntax_policy)

    def build(self) -> list[QueryStatement]:
        statement = QueryStatement(expression='', is_bulk_params=True)

        self.__append_insert_into(statement)

        self.__append_values_statement(statement)

        return [statement]

    def __append_insert_into(self, statement: QueryStatement):
        columns_expression = \
            f"({', '.join([self.component_compiler.compile(c).expression for c in self.query.columns])})"

        table_expression = self.component_compiler.compile(self.query.table).expression

        statement.expression += f"INSERT INTO {table_expression} {columns_expression} "

    def __append_values_statement(self, statement: QueryStatement):
        values_expression = f"VALUES({', '.join([QUERY_PARAM_PLACEHOLDER for _ in self.query.values[0]])})"
        statement.expression += values_expression

        statement.extend_params(self.__create_values_query_params())

    def __create_values_query_params(self) -> [QueryParam]:
        columns_count = len(self.query.columns)
        params = []

        for i in range(columns_count):
            column_values = [row[i] for row in self.query.values]
            params.append(QueryParam(value=column_values))

        return params
