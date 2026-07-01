FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        default-jdk \
        curl \
        procps && \
    rm -rf /var/lib/apt/lists/*

COPY spark/requirements/requirements-base.txt .

RUN pip install --no-cache-dir \
    -r requirements-base.txt

COPY spark/requirements/requirements-platform.txt .

RUN pip install --no-cache-dir \
    -r requirements-platform.txt

COPY spark /app/spark

CMD ["tail", "-f", "/dev/null"]