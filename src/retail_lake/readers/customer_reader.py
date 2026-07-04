from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

from retail_lake.config.settings import RAW_CUSTOMER_PATH


def read_customer_file(spark: SparkSession) -> DataFrame:

    return (
        spark.read
        .option("header", True)
        .csv(RAW_CUSTOMER_PATH)
    )