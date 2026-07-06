from abc import ABC, abstractmethod

class PipelineService(ABC):

    @abstractmethod
    def execute(self, spark):

        """
        Execute complete pipeline workflow.
        """
        pass