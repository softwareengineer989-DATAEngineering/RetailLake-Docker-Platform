# RetailLake Docker Platform

Enterprise-grade Data Engineering Platform.

## Overview

Production-style Docker platform with PySpark, PostgreSQL, Airflow,
DuckDB, layered architecture, audit logging, metrics and reusable
pipelines.

## Architecture

``` text
Platform Launcher -> Pipeline Factory -> Customer Pipeline -> Reader -> Validator -> Transformer -> Writer -> Storage
```

## Technology Stack

-   Docker
-   Docker Compose
-   Python 3.13
-   PySpark
-   PostgreSQL
-   Airflow
-   DuckDB
-   dbt
-   Kafka (scaffold)

## Repository Structure

``` text
airflow/
docker/
requirements/
src/
data/
postgres/
duckdb/
docs/
tests/
```

## Build

``` bash
docker compose --profile full build
```

## Run

``` bash
docker compose --profile full up -d
```

## Execute Pipeline

``` bash
docker exec retail-spark spark-submit /app/src/retail_lake/launcher/platform_launcher.py customer
```

## Engineering Practices

-   Feature branches
-   Pull Requests
-   Centralized configuration
-   Platform Context
-   Factory pattern
-   Separation of concerns

## Future Roadmap

-   Kafka Streaming
-   Delta Lake
-   CI/CD
-   Monitoring
