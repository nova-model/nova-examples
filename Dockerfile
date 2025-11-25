FROM python:3.13-slim

RUN apt update && apt install -y \
    curl \
    g++ \
    libosmesa6-dev \
    libx11-dev \
    libxrender1

RUN curl -fsSL https://pixi.sh/install.sh | sh
ENV PATH="/root/.pixi/bin:${PATH}"

RUN mkdir -p /opt/run/examples
COPY examples/ /opt/run/examples/
COPY tests/ /opt/run/
COPY pyproject.toml /opt/run/pyproject.toml

WORKDIR /opt/run
RUN pixi install
SHELL [ "pixi", "run" ]
ENTRYPOINT [ "pixi", "run" ]

CMD []
