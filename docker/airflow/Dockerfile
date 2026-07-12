FROM apache/airflow:3.0.2-python3.12

USER root

RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean

USER airflow

COPY requirements/base.txt requirements/
COPY requirements/airflow.txt requirements/

RUN pip install --no-cache-dir \
    -r requirements/airflow.txt