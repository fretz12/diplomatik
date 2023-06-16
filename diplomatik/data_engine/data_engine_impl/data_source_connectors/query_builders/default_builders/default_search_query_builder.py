from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.source_extraction_builders.source_extraction_builder_factory import \
    SourceExtractionBuilderFactory
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder import QueryBuilder
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler_factory import \
    QueryComponentCompilerFactory
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy_factory import \
    SyntaxPolicyFactory
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.query.search_query import SearchQuery
from diplomatik.data_model.source_extraction.source_extraction import SourceExtractionType


class DefaultSearchQueryBuilder(QueryBuilder):
    def __init__(self, source_type: DataSourceType, search_query: SearchQuery):
        self.search_query = search_query

        syntax_policy = SyntaxPolicyFactory.construct(source_type)
        component_compiler = QueryComponentCompilerFactory.construct(source_type, syntax_policy)

        extraction_type = SourceExtractionType.get_by_value(search_query.source_extraction.extraction_type)

        self.source_extraction_builder = SourceExtractionBuilderFactory.construct(
            extraction_type, component_compiler, syntax_policy, search_query.source_extraction)

    def build(self) -> list[QueryStatement]:
        return [self.source_extraction_builder.build()]
