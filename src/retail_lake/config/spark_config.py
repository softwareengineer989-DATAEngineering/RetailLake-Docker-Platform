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

        .config(
            "spark.driver.extraJavaOptions",
            "-Dlog4j.configurationFile=/opt/spark/conf/log4j2.properties"
        )

        .config(
            "spark.executor.extraJavaOptions",
            "-Dlog4j.configurationFile=/opt/spark/conf/log4j2.properties"
        )


        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")


    return spark