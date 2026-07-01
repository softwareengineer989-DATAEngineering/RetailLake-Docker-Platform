FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        default-jdk \
        curl \
        procps && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="${JAVA_HOME}/bin:${PATH}"

COPY spark/requirements/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY spark /app/spark

CMD ["tail", "-f", "/dev/null"]