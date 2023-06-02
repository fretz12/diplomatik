from typing import TypeVar, Generic

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.column_component_compiler import \
    ColumnComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.limit_offset_compiler import \
    LimitOffsetCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.source_formation_compilers.source_formation_component_compiler import \
    SourceFormationComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.table_component_compiler import \
    TableComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.value_component_compiler import \
    ValueComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.data_source_type import DataSourceType
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.query_component import QueryComponent, QueryComponentType
from diplomatik.exceptions.exceptions import DataEngineException

T = TypeVar("T", bound=QueryComponent)


class DefaultQueryComponentCompiler(QueryComponentCompiler, Generic[T]):
    def __init__(self, source_type: DataSourceType, syntax_policy: SyntaxPolicy):
        self.source_type = source_type
        self.syntax_policy = syntax_policy

    def compile(self, component: T) -> QueryStatement:
        component_type = component.component_type

        if component_type == QueryComponentType.aggregation:
            pass
        elif component_type == QueryComponentType.column:
            return ColumnComponentCompiler(self.syntax_policy).compile(component)
        elif component_type == QueryComponentType.filter:
            pass
        elif component_type == QueryComponentType.function:
            pass
        elif component_type == QueryComponentType.group_by:
            pass
        elif component_type == QueryComponentType.limit_offset:
            LimitOffsetCompiler(self.syntax_policy).compile(component)
        elif component_type == QueryComponentType.order_by:
            pass
        elif component_type == QueryComponentType.source_formation:
            return SourceFormationComponentCompiler(self.syntax_policy).compile(component)
        elif component_type == QueryComponentType.table:
            return TableComponentCompiler(self.syntax_policy).compile(component)
        elif component_type == QueryComponentType.value:
            return ValueComponentCompiler(self.syntax_policy, self).compile(component)
        elif component_type == QueryComponentType.view:
            pass

        raise DataEngineException(f'Unsupported query component type: {component_type}')
