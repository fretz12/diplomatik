from diplomatik.data_model.query.event_hooks.event_hook import EventHook, EventHookExecutionOrder, EventHookType
from diplomatik.data_model.table_management.columns.column_definition import CreateColumnDefinition


class TableColumnsAddedEventHook(EventHook):
    column_definitions: list[CreateColumnDefinition] | None = None

    def __init__(self, execution_order: EventHookExecutionOrder = EventHookExecutionOrder.post_query, **data):
        super().__init__(event_hook_type=EventHookType.table_columns_added, execution_order=execution_order,
                         **data)
