from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_builders.default_builders.data_source_management_builders.data_source_management_builder import \
    DataSourceManagementBuilder
from diplomatik.data_model.query.field import FieldDataType
from diplomatik.data_model.query.query_statement import QueryStatement
from diplomatik.data_model.table_management.columns.column_definition import CreateColumnDefinition, \
    CreateColumnDefinitionUnion
from diplomatik.data_model.table_management.create_table_command import CreateTableCommand
from diplomatik.exceptions.exceptions import DataEngineException


class CreateTableBuilder(DataSourceManagementBuilder[CreateTableCommand]):
    def build(self) -> QueryStatement:
        command = self.management_command

        column_expressions = [self.__build_create_table_column_expression(column)
                              for column in command.column_definitions]

        if_not_exists_expression = ' IF NOT EXISTS' if command.if_not_exists else ''

        expression = f"CREATE TABLE{if_not_exists_expression} {command.table_name} ({', '.join(column_expressions)})"

        return QueryStatement(expression=expression)

    def __build_create_table_column_expression(self, column_definition: CreateColumnDefinitionUnion):
        data_type = self.__get_data_type(column_definition)
        extra_definitions = column_definition.extra_definitions if column_definition.extra_definitions else ''

        return f"{column_definition.column_name} {data_type} {extra_definitions}"

    def __get_data_type(self, column_definition: CreateColumnDefinitionUnion):
        data_type = FieldDataType.get_by_value(column_definition.data_type)

        if data_type == FieldDataType.int32:
            return 'INT'
        elif data_type == FieldDataType.int64:
            return 'BIGINT'
        elif data_type == FieldDataType.float32:
            return 'FLOAT'
        elif data_type == FieldDataType.float64:
            return 'DOUBLE PRECISION'
        elif data_type == FieldDataType.string:
            return f"VARCHAR({column_definition.byte_count})"
        elif data_type == FieldDataType.date:
            return 'DATE'
        elif data_type == FieldDataType.auto_increment_int:
            return 'SERIAL'
        else:
            raise DataEngineException(f"Unsupported column data type: {column_definition.data_type}")
