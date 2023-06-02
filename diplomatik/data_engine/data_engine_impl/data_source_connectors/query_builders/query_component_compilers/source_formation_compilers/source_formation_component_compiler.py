from typing import TypeVar

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.source_formation_compilers.single_table_formation_compiler import \
    SingleTableFormationCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.query_component import QueryComponent
from diplomatik.data_model.source_formation.source_formation import SourceFormationType
from diplomatik.exceptions.exceptions import DataEngineException

T = TypeVar("T", bound=QueryComponent)


class SourceFormationComponentCompiler(QueryComponentCompiler[T]):
    def __init__(self, syntax_policy: SyntaxPolicy):
        self.syntax_policy = syntax_policy

    def compile(self, source_formation: T) -> QueryStatement:
        formation_type = SourceFormationType.get_by_value(source_formation.formation_type)

        if formation_type == SourceFormationType.single_table:
            return SingleTableFormationCompiler(syntax_policy=self.syntax_policy).compile(source_formation)
        elif formation_type == SourceFormationType.join:
            ## TODO
            pass

        raise DataEngineException(f"Unknown source formation type: {source_formation.formation_type}")
