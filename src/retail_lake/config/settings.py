from dotenv import load_dotenv
import os

load_dotenv()

# PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_CONTAINER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# DuckDB
DUCKDB_PATH = "/app/duckdb/database/retaillake.duckdb"

# Input files
RAW_CUSTOMER_PATH = "/app/data/raw/customers.csv"

# Output files
PROCESSED_CUSTOMER_PATH = "/app/data/processed/customers"