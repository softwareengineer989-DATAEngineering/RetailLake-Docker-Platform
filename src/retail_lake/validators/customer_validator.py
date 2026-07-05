from retail_lake.quality.quality_engine import DataQualityEngine
from retail_lake.utils.logger import get_logger

def validate_customer_data(df):

    logger = get_logger("CustomerValidator")

    logger.info("Starting validation")

    logger.info("Validation completed")

    engine = DataQualityEngine()

    report = engine.run(df)

    logger.info(report.summary())

    print(report.summary())

    return report