from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.filter_compilers.default_bound_filter_compiler import \
    DefaultBoundFilterCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.filter_compilers.default_equals_filter_compiler import \
    DefaultEqualsFilterCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy
from diplomatik.data_model.filter.filter import Filter, FilterType
from diplomatik.data_model.query.query_statement import QueryStatement, QueryParam
from diplomatik.exceptions.exceptions import DataEngineException


class DefaultFilterComponentCompiler(QueryComponentCompiler[Filter]):
    def __init__(self, syntax_policy: SyntaxPolicy, query_component_compiler: QueryComponentCompiler):
        self.syntax_policy = syntax_policy
        self.query_component_compiler = query_component_compiler

    def compile(self, filter: Filter) -> QueryStatement:
        filter_stack = [filter]
        boolean_operator_stack = []
        visited_filter_ids = set()
        expression_stack = []
        statement_params = []

        while filter_stack:
            current_filter = filter_stack.pop()

            if self.__is_nested_filter(current_filter):
                self.__process_nested_filter(current_filter, visited_filter_ids, expression_stack, boolean_operator_stack,
                                             filter_stack)
            else:
                self.__process_filter(current_filter, expression_stack, statement_params, boolean_operator_stack)

        return QueryStatement(expression=f"{' '.join(expression_stack)} ", params=statement_params)

    def __is_nested_filter(self, filter: Filter):
        return filter.get_filter_type() == FilterType.and_condition or \
            filter.get_filter_type() == FilterType.or_condition

    def __process_nested_filter(self, current_filter: Filter,
                                visited_filter_ids: set[int],
                                expression_stack: list[str],
                                boolean_operator_stack: [str],
                                filter_stack: list[Filter]):
        if id(current_filter) in visited_filter_ids:
            if expression_stack[-1] == current_filter.get_boolean_operator_expression():
                expression_stack.pop()

            expression_stack.append(')')
            boolean_operator_stack.pop()

            self.__append_boolean_operator_if_needed(boolean_operator_stack, expression_stack)
        else:
            expression_stack.append('(')
            visited_filter_ids.add(id(current_filter))
            filter_stack.append(current_filter)
            filter_stack.extend(current_filter.get_children_filters())
            boolean_operator_stack.append(current_filter.get_boolean_operator_expression())

    def __process_filter(self, current_filter: Filter, expression_stack: list[str], params: list[QueryParam],
                         boolean_operator_stack: [str]):
        statement = self.__compile_filter(current_filter)

        expression_stack.append(statement.expression)

        params.extend(statement.params)

        self.__append_boolean_operator_if_needed(boolean_operator_stack, expression_stack)

    def __append_boolean_operator_if_needed(self, boolean_operator_stack: [str], expression_stack: list[str]):
        if not boolean_operator_stack:
            return

        expression_stack.append(boolean_operator_stack[-1])

    def __compile_filter(self, filter: Filter) -> QueryStatement:
        filter_type = filter.get_filter_type()

        if filter_type == FilterType.bound:
            return DefaultBoundFilterCompiler(self.syntax_policy, self.query_component_compiler).compile(filter)
        elif filter_type == FilterType.equals:
            return DefaultEqualsFilterCompiler(self.syntax_policy, self.query_component_compiler).compile(filter)
        else:
            raise DataEngineException(f"Unknown filter type: {filter_type}")
