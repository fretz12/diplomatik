from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.source_extraction_builders.source_extraction_builder_factory import \
    SourceExtractionBuilderFactory
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.filter.in_subselect_filter import InSubSelectFilter
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.source_extraction.source_extraction import SourceExtractionType


class DefaultInSubSelectFilterCompiler(QueryComponentCompiler[InSubSelectFilter]):
    def __init__(self, syntax_policy: SyntaxPolicy, query_component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.query_component_compiler = query_component_compiler

    def compile(self, filter: InSubSelectFilter) -> QueryStatement:
        statement = QueryStatement(expression='', params=[])

        field_statement = self.query_component_compiler.compile(filter.field)

        sub_select_statement = self.__create_subselect_statement(filter)

        in_expression = 'NOT IN' if filter.negate else 'IN'

        expression = f"{field_statement.expression} {in_expression} ({sub_select_statement.expression})"

        statement.extend_params(field_statement.params)
        statement.extend_params(sub_select_statement.params)

        statement.expression += expression

        return statement

    def __create_subselect_statement(self, filter: InSubSelectFilter) -> QueryStatement:
        filter.select_extraction.distinct = True

        source_extraction_builder = SourceExtractionBuilderFactory.construct(
            SourceExtractionType.get_by_value(filter.select_extraction.extraction_type), self.query_component_compiler,
            self.syntax_policy, filter.select_extraction)

        subselect_statement = source_extraction_builder.build()

        return subselect_statement
