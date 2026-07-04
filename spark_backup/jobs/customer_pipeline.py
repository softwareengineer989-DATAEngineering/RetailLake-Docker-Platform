from pyspark.sql import SparkSession

from readers.customer_reader import read_customer_file
from transformers.customer_transformer import transform_customer_data
from validators.customer_validator import validate_customer_data
from writers.customer_writer import write_customer_data


def main():

    spark = (
        SparkSession.builder
        .appName("RetailLake Customer Pipeline")
        .getOrCreate()
    )

    df = read_customer_file(spark)

    validate_customer_data(df)

    df = transform_customer_data(df)

    write_customer_data(df)

    spark.stop()


if __name__ == "__main__":
    main()