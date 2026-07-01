import duckdb

from src.config.settings import DUCKDB_PATH

connection = duckdb.connect(DUCKDB_PATH)