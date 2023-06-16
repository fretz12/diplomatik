from diplomatik.data_model.query.query_results.query_result import QueryResultType, QueryResult


class PyDictQueryResult(QueryResult):
    results: list[dict]

    def __init__(self, query_id: str | None = None, **data):
        super().__init__(result_type=QueryResultType.py_dict, query_id=query_id, **data)
