from fastapi import APIRouter, Body

from diplomatik.data_engine.data_engine_api.data_engine_factory import DataEngineFactory
from diplomatik.data_model.query.query_data_types import QueryUnionBody

router = APIRouter(
    prefix="/queries",
    tags=["queries"],
    responses={404: {"description": "Not found"}},
)


@router.post("/read")
async def read(query: QueryUnionBody):
    return DataEngineFactory.create_engine().execute_read_query(query)


@router.post("/write")
async def write(query: QueryUnionBody):
    DataEngineFactory.create_engine().execute_write_query(query)
