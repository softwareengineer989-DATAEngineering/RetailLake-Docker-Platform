from pyspark.sql import SparkSession
from retail_lake.config.settings import RAW_CUSTOMER_PATH
from retail_lake.utils.logger import get_logger


logger = get_logger("CustomerReader")

def read_customer_file(spark: SparkSession):

    logger.info("=" * 60)
    logger.info("Reading customer file")
    logger.info(f"Source : {RAW_CUSTOMER_PATH}")

    df = (
        spark.read
        .option("header", True)
        .csv(RAW_CUSTOMER_PATH)
    )

    logger.info(f"Records Read : {df.count()}")

    return df