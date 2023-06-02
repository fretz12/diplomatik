from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.syntax_policies.syntax_policy import \
    SyntaxPolicy


class PostgresSyntaxPolicy(SyntaxPolicy):
    def to_sql_identifier(self, identifier: str):
        return f"\"{identifier}\""

    def to_sql_string_literal(self, value: str) -> str:
        return f"'{value}'"
