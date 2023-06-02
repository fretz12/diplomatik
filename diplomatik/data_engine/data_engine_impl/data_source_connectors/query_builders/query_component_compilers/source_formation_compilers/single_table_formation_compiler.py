from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.table_component_compiler import \
    TableComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.source_formation.single_table_formation import SingleTableFormation


class SingleTableFormationCompiler(QueryComponentCompiler[SingleTableFormation]):
    def __init__(self, syntax_policy: SyntaxPolicy):
        self.syntax_policy = syntax_policy

    def compile(self, source_formation: SingleTableFormation) -> QueryStatement:
        return TableComponentCompiler(syntax_policy=self.syntax_policy).compile(source_formation.table)
