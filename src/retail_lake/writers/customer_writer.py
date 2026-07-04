from pyspark.sql import DataFrame

from retail_lake.config.settings import PROCESSED_CUSTOMER_PATH

def write_customer_data(df: DataFrame):

    (
        df.write
        .mode("overwrite")
        .parquet(PROCESSED_CUSTOMER_PATH)
    )