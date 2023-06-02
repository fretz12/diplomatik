from __future__ import annotations

from sqlalchemy import Result

from diplomatik.data_engine.data_engine_impl.data_source_connectors.query_executors.query_result_adapters.query_result_adapter import \
    QueryResultAdapter
from diplomatik.data_model.query.query_results.pydict_query_result import PyDictQueryResult


class SqlAlchemyPydictAdapter(QueryResultAdapter[Result, PyDictQueryResult]):
    def parse(self, result: Result) -> PyDictQueryResult:
        return PyDictQueryResult(results=result.mappings().all())
