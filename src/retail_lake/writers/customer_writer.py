from retail_lake.config.settings import PROCESSED_CUSTOMER_PATH
from retail_lake.utils.logger import get_logger

logger = get_logger("CustomerWriter")


def write_customer_data(df):

    logger.info("=" * 60)
    logger.info("Writing parquet dataset")

    (
        df.write
        .mode("overwrite")
        .parquet(PROCESSED_CUSTOMER_PATH)
    )

    logger.info(f"Target : {PROCESSED_CUSTOMER_PATH}")
    logger.info("Write completed")