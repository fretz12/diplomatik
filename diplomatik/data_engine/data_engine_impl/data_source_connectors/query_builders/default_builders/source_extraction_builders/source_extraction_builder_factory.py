from typing import TypeVar

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.source_extraction_builders.select_extraction_builder import \
    SelectExtractionBuilder
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction, SourceExtractionType

T = TypeVar("T", bound=SourceExtraction)


class SourceExtractionBuilderFactory:
    @staticmethod
    def construct(source_extraction_type: SourceExtractionType, component_compiler: QueryComponentCompiler,
                  syntax_policy: SyntaxPolicy, source_extraction: T):
        builders = {
            SourceExtractionType.select: SelectExtractionBuilder,
        }

        return builders[source_extraction_type](component_compiler, syntax_policy, source_extraction)
