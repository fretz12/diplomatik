from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_builder_utils import \
    compile_append_query_component
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.source_extraction.source_extraction import SourceExtraction


T = TypeVar("T", bound=SourceExtraction)


class SourceExtractionBuilder(ABC, Generic[T]):
    def __init__(self, component_compiler: QueryComponentCompiler, syntax_policy: SyntaxPolicy,
                 source_extraction: T):
        self.component_compiler = component_compiler
        self.syntax_policy = syntax_policy
        self.source_extraction = source_extraction

    @abstractmethod
    def build(self):
        pass

    def append_where_clause(self, statement: QueryStatement) -> QueryStatement:
        return compile_append_query_component(statement, self.source_extraction.filter, self.component_compiler,
                                              component_prefix='WHERE ')

    def append_order_by(self, statement: QueryStatement) -> QueryStatement:
        return compile_append_query_component(statement, self.source_extraction.order_by, self.component_compiler)
