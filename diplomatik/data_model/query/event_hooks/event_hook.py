from enum import Enum

from pydantic import BaseModel

from diplomatik.exceptions.exceptions import DataModelException


class EventHookType(Enum):
    """
    The type of event hook
    """
    table_columns_added = "table_columns_added"
    table_columns_deleted = "table_columns_deleted"
    table_data_changed = "table_data_changed"
    table_created = "table_created"
    table_deleted = "table_deleted"

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the event hook type enum by value

        :param value: the value to get from
        :return: the matching event hook type
        :rtype: EventHookType
        """
        for type in EventHookType:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid event hook type")


class EventHookExecutionOrder(Enum):
    pre_query = "pre_query"
    post_query = "post_query"

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the event hook execution order enum by value

        :param value: the value to get from
        :return: the matching event hook execution order type
        :rtype: EventHookExecutionOrder
        """
        for type in EventHookExecutionOrder:
            if type.value == value:
                return type

        raise DataModelException(f"{value} is not a valid event hook execution order")


class EventHook(BaseModel):
    """
    Event hooks are callbacks that get executed either before or after a query gets executed
    """
    event_hook_type: EventHookType
    """The event hook type"""

    execution_order: EventHookExecutionOrder = EventHookExecutionOrder.post_query
    """The order of whether to execute the event hook before or after the query execution"""
