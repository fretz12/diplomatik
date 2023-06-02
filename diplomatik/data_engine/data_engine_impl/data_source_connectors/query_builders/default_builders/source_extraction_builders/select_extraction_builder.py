from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.source_extraction_builders.source_extraction_builder import \
    SourceExtractionBuilder
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder_utils import \
    compile_append_query_component
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.source_formation_compilers.source_formation_component_compiler import \
    SourceFormationComponentCompiler
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.source_extraction.select_extraction import SelectExtraction


class SelectExtractionBuilder(SourceExtractionBuilder[SelectExtraction]):
    def build(self):
        statement = self.__create_select_from()

        statement = self.append_where_clause(statement)

        statement = self.append_order_by(statement)

        statement = self.__append_offset_limit(statement)

        return statement

    def __create_select_from(self):
        statement = QueryStatement(expression='', params=[])

        distinct = 'DISTINCT ' if self.source_extraction.distinct else ''

        columns_statement = self.__create_select_columns_statement()

        source_formation_statement = SourceFormationComponentCompiler(syntax_policy=self.syntax_policy)\
            .compile(self.source_extraction.source_formation)

        statement.expression = f"SELECT {distinct}{columns_statement.expression} " \
                               f"FROM {source_formation_statement.expression} "

        statement.extend_params(columns_statement.params)
        statement.extend_params(source_formation_statement.params)

        return statement

    def __create_select_columns_statement(self) -> QueryStatement:
        select_column_statements = [self.component_compiler.compile(field) for field in self.source_extraction.fields]

        select_expression = ', '.join([statement.expression for statement in select_column_statements])

        select_params = []
        for statement in select_column_statements:
            if statement.params:
                select_params.extend(statement.params)

        return QueryStatement(expression=select_expression, params=select_params)

    def __append_offset_limit(self, statement: QueryStatement) -> QueryStatement:
        return compile_append_query_component(statement, self.source_extraction.pagination, self.component_compiler)
