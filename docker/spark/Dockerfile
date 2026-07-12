FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        default-jdk \
        curl \
        wget \
        unzip \
        procps && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PYTHONPATH=/app/src

# ----------------------------
# Python Dependencies
# ----------------------------

COPY requirements/base.txt requirements/
COPY requirements/spark.txt requirements/

RUN pip install --no-cache-dir \
    -r requirements/spark.txt

# ----------------------------
# Application Code
# ----------------------------

COPY src /app/src

# ----------------------------
# Data
# ----------------------------

COPY data /app/data

# ----------------------------
# DuckDB
# ----------------------------

COPY duckdb /app/duckdb

# ----------------------------
# Spark Logging
# ----------------------------

COPY docker/spark/conf/log4j2.properties \
     /opt/spark/conf/log4j2.properties

CMD ["tail","-f","/dev/null"]