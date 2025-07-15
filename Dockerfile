FROM python:3.13-alpine

RUN mkdir -p /opt/run/examples
COPY examples/ /opt/run/examples/
COPY tests/ /opt/run/
COPY pyproject.toml /opt/run/pyproject.toml

WORKDIR /opt/run
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry install

CMD []
