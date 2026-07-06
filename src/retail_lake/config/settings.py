from dotenv import load_dotenv
import os

load_dotenv()

# -------------------------------------------------------
# Project
# -------------------------------------------------------

APP_NAME = os.getenv(
    "APP_NAME",
    "RetailLake Platform"
)

Environment = os.getenv(
    "ENVIRONMENT",
    "dev"
)

# -------------------------------------------------------
# PostgreSQL
# -------------------------------------------------------


POSTGRES_HOST = os.getenv("POSTGRES_CONTAINER")

POSTGRES_DB = os.getenv("POSTGRES_DB")

POSTGRES_USER = os.getenv("POSTGRES_USER")

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# -------------------------------------------------------
# DuckDB
# -------------------------------------------------------

DUCKDB_PATH = os.getenv(
    "DUCKDB_PATH",
    "/app/duckdb/database/retaillake.duckdb"
)

# -------------------------------------------------------
# Input Data
# -------------------------------------------------------

RAW_CUSTOMER_PATH = os.getenv(
    "RAW_CUSTOMER_PATH",
    "/app/data/raw/customers.csv"
)

# -------------------------------------------------------
# Output Data
# -------------------------------------------------------

PROCESSED_CUSTOMER_PATH = os.getenv(
    "PROCESSED_CUSTOMER_PATH",
    "/app/data/processed/customers"
)