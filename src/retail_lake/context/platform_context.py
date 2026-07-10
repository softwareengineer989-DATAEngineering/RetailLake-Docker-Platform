from retail_lake.audit.audit_record import AuditRecord
from retail_lake.metrics.pipeline_metrics import PipelineMetrics
from retail_lake.utils.logger import get_logger
from retail_lake.config import settings
import uuid

class PlatformContext:

    def __init__(self, pipeline_name: str):

        self.execution_id = str(uuid.uuid4())

        self.pipeline_name = pipeline_name

        self.settings = settings

        self.environment = settings.Environment

        self.logger = get_logger(pipeline_name)

        self.audit = AuditRecord(pipeline_name)

        self.metrics = PipelineMetrics()

        self.spark = None