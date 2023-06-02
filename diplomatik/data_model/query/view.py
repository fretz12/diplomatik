from diplomatik.data_model.query_component import QueryComponent, QueryComponentType


class View(QueryComponent):
    """
    Definition for creating a logical view. Implementation is dependent on data source type.
    """
    view_name: str
    """Name of the view"""

    def __init__(self, **data):
        super().__init__(component_type=QueryComponentType.view, **data)