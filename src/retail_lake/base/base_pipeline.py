from abc import ABC, abstractmethod

from retail_lake.utils.logger import get_logger
from retail_lake.metrics.pipeline_metrics import PipelineMetrics


class BasePipeline(ABC):

    def __init__(self, pipeline_name: str):

        self.logger = get_logger(pipeline_name)
        self.metrics = PipelineMetrics()

    def start(self):

        self.metrics.start()

        self.logger.info("=" * 60)
        self.logger.info(f"Starting {self.__class__.__name__}")
        self.logger.info("=" * 60)

    def finish(self):

        self.metrics.stop()


        self.logger.info("=" * 60)
        self.logger.info(f"Completed {self.__class__.__name__}")
        self.logger.info(
            f"Execution Time: {self.metrics.duration} seconds"
        )
        self.logger.info("=" * 60)

    @abstractmethod
    def run(self):
        pass


















