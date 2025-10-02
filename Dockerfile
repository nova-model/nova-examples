FROM python:3.13-slim

RUN apt update && apt install -y \
    curl \
    g++ \
    libosmesa6-dev \
    libx11-dev \
    libxrender1

ENV POETRY_HOME=/poetry
ENV PATH=/poetry/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN mkdir -p /opt/run/examples
COPY examples/ /opt/run/examples/
COPY tests/ /opt/run/
COPY pyproject.toml /opt/run/pyproject.toml
COPY poetry.lock /opt/run/poetry.lock

WORKDIR /opt/run
RUN poetry install

CMD []
