import duckdb

database = duckdb.connect(

"/app/duckdb/database/retaillake.duckdb"

)

database.execute("""

INSERT INTO customers

VALUES

(1,'John','New York','USA'),

(2,'Alice','London','UK'),

(3,'David','Mumbai','India')

""")

print(database.execute(

"SELECT * FROM customers"

).fetchdf())