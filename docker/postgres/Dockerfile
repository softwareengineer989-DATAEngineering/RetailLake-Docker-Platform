FROM postgres:17.10

LABEL maintainer="softwareengineer989-DATAEngineering"

LABEL project="RetailLake Docker Platform"

LABEL service="PostgreSQL"

WORKDIR /docker-entrypoint-initdb.d

COPY postgres/init/ .

EXPOSE 5432