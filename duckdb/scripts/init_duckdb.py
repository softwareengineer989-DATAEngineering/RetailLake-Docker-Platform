import duckdb

database = duckdb.connect(

    "/app/duckdb/database/retaillake.duckdb"

)

database.execute("""

CREATE TABLE IF NOT EXISTS customers (

customer_id INTEGER,

customer_name VARCHAR,

city VARCHAR,

country VARCHAR

)

""")

print("DuckDB Initialized")