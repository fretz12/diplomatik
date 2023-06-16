from fastapi import FastAPI

from diplomatik.transports.fastapi.routers import queries


app = FastAPI()

app.include_router(queries.router)
