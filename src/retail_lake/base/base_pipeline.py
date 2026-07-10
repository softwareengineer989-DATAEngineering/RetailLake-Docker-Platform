from abc import ABC, abstractmethod

from retail_lake.audit.audit_record import AuditRecord
from retail_lake.utils.logger import get_logger
from retail_lake.metrics.pipeline_metrics import PipelineMetrics
from retail_lake.config.logging_config import configure_logging

class BasePipeline(ABC):

    def __init__(self, context):
        configure_logging()

        self.context = context

        self.logger = context.logger

        self.metrics = context.metrics

        self.audit = context.audit

    def start(self):

        self.metrics.start()

        self.logger.info(
            f"Execution ID : {self.audit.execution_id}"
        )

        self.logger.info(
            f"Pipeline Name : {self.audit.pipeline_name}"
        )

        self.logger.info("=" * 60)
        self.logger.info(f"Starting {self.__class__.__name__}")
        self.logger.info("=" * 60)

    def finish(self):
        from retail_lake.audit.audit_logger import AuditLogger

        self.audit.complete("SUCCESS")

        self.metrics.stop()

        AuditLogger.log(self.audit)

        self.logger.info(
            f"Execution Status : {self.audit.status}"
        )

        self.logger.info(
            f"Execution Duration : {self.metrics.duration:.2f} seconds"
        )



        self.logger.info("=" * 60)
        self.logger.info(f"Completed {self.__class__.__name__}")
        self.logger.info(
            f"Execution Time: {self.metrics.duration} seconds"
        )
        self.logger.info("=" * 60)

    @abstractmethod
    def run(self):
        pass


















