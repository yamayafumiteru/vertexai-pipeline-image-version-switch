FROM python:3.10

RUN pip install poetry

WORKDIR /app
COPY . .
RUN poetry install
