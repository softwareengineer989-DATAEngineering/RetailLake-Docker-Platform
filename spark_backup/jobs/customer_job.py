from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("RetailLake")
    .getOrCreate()
)

data = [

    (1, "John"),

    (2, "Alice"),

    (3, "David")

]

df = spark.createDataFrame(

    data,

    ["customer_id", "customer_name"]

)

df.show()

print("RetailLake Spark Runtime Working")

spark.stop()