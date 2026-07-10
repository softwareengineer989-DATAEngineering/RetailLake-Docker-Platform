
from retail_lake.base.base_pipeline import BasePipeline
from retail_lake.config.spark_config import create_spark_session
from retail_lake.services.customer_service import CustomerService


class CustomerPipeline(BasePipeline):

    def __init__(self):
        super().__init__("CustomerPipeline")

    def run(self):

        spark = create_spark_session()

        service = CustomerService()

        result = service.execute(spark)

        report = result["report"]

        self.audit.records_read = result["records_read"]

        self.audit.records_written = result["records_written"]

        self.audit.records_rejected = (
                report.null_records
                + report.duplicate_records
        )

        spark.stop()


from retail_lake.registry.pipeline_registry import (
    register_pipeline,
    get_pipeline
)

register_pipeline(
    "customer",
    CustomerPipeline
)

