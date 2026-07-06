from retail_lake.services.pipeline_service import PipelineService

from retail_lake.readers.customer_reader import read_customer_file

from retail_lake.validators.customer_validator import validate_customer_data

from retail_lake.transformers.customer_transformer import transform_customer_data

from retail_lake.writers.customer_writer import write_customer_data


class CustomerService(PipelineService):

    def execute(self, spark):

        df = read_customer_file(spark)

        report = validate_customer_data(df)

        transformed_df = transform_customer_data(df)

        write_customer_data(transformed_df)

        return {

            "report": report,

            "records_read": df.count(),

            "records_written": transformed_df.count()

        }