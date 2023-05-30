from diplomatik.data_engine.data_engine_api.query_component import QueryComponent


class View(QueryComponent):
    """
    Definition for creating a logical view. Implementation is dependent on data source type.
    """
    view_name: str
    """Name of the view"""
