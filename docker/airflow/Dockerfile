FROM apache/airflow:3.0.2-python3.12

USER root

RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean

USER airflow

COPY airflow/requirements/requirements-base.txt .

RUN pip install --no-cache-dir \
    -r requirements-base.txt

COPY airflow/requirements/requirements-platform.txt .

RUN pip install --no-cache-dir \
    -r requirements-platform.txt