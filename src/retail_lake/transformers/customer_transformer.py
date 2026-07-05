from pyspark.sql.functions import upper
from retail_lake.utils.logger import get_logger

logger = get_logger("CustomerTransformer")


def transform_customer_data(df):

    logger.info("Applying transformations")

    transformed_df = (
        df.withColumn(
            "country",
            upper(df.country)
        )
    )

    logger.info("Transformation completed")

    return transformed_df