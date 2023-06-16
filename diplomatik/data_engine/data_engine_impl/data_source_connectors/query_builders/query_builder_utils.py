from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.query_component_compilers.query_component_compiler import \
    QueryComponentCompiler
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.query_component import QueryComponent


def compile_append_query_component(statement: QueryStatement,
                                   query_component: QueryComponent | None,
                                   component_compiler: QueryComponentCompiler,
                                   component_prefix: str = '') -> QueryStatement:
    """
    Compiles a query component into a statement and appends it to an existing statement

    :param statement: the statement to append to
    :param query_component: the query component to compile
    :param component_compiler: the component compiler to use
    :return: the appended statement
    """
    if not query_component:
        return statement

    component_statement = component_compiler.compile(query_component)

    statement.expression = statement.expression + component_prefix + component_statement.expression
    statement.params.extend(component_statement.params)

    return statement
