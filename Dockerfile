FROM python:3.10.6

ENV POETRY_VERSION=1.4.2

COPY poetry.lock pyproject.toml /backend/
WORKDIR /backend

RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /backend
