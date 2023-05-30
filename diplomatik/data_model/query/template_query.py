from enum import Enum

from diplomatik.data_model.query.event_hooks.event_hook import EventHook
from diplomatik.data_model.query.query import Query, QueryType, DataSourceConfig, QueryResultConfig
from diplomatik.exceptions.exceptions import DataModelException


class TemplateQueryId(Enum):
    deduplicate_rows = 'deduplicate_rows'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the template query ID based on its string value

        :param value: the value to match
        :return: the template query ID
        """
        for id in TemplateQueryId:
            if id.value == value:
                return id

        raise DataModelException(f"{value} is not a valid template query ID")


class TemplateQuery(Query):
    """Query which can execute custom SQL stored in templates"""
    template_id: TemplateQueryId = None,
    """The template query ID"""

    variables: dict = None
    """Arbitrary key value pair variables used as part of the query"""

    def __init__(self, data_source_config: DataSourceConfig, query_result_config: QueryResultConfig = None,
                 query_id: str | None = None, event_hooks: [EventHook] = None, **data):
        super().__init__(query_type=QueryType.template,
                         data_source_config=data_source_config,
                         query_result_config=query_result_config,
                         query_id=query_id,
                         event_hooks=event_hooks,
                         **data)
