from pyspark.sql import SparkSession

from retail_lake.config import settings

def create_spark_session():

    spark = (
        SparkSession.builder
        .appName(settings.APP_NAME)

        .config(
            "spark.sql.shuffle.partitions",
            "8"
        )

        .config(
            "spark.sql.adaptive.enabled",
            "true"
        )

        .config(
            "spark.sql.adaptive.coalescePartitions.enabled",
            "true"
        )

        .config(
            "spark.sql.session.timeZone",
            "UTC"
        )

        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")


    return spark