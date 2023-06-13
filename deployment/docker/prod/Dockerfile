FROM python:3.11.4-slim-buster

WORKDIR /app

ENV POETRY_VERSION=1.5.1

RUN pip3 install poetry==$POETRY_VERSION

COPY . .

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

ENTRYPOINT uvicorn diplomatik.transports.fastapi.main:app
