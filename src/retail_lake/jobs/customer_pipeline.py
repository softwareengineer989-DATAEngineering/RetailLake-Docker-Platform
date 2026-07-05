from pyspark.sql import SparkSession

from retail_lake.base.base_pipeline import BasePipeline
from retail_lake.readers.customer_reader import read_customer_file
from retail_lake.transformers.customer_transformer import transform_customer_data
from retail_lake.validators.customer_validator import validate_customer_data
from retail_lake.writers.customer_writer import write_customer_data


class CustomerPipeline(BasePipeline):

    def __init__(self):
        super().__init__("CustomerPipeline")

    def run(self):

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
    
    pipeline = CustomerPipeline()

    try:

        pipeline.start()

        pipeline.run()

        pipeline.finish()

    except Exception as e:
        pipeline.logger.exception(e)

        raise