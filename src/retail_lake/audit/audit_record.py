from datetime import datetime
import uuid

class AuditRecord:

    def __init__(self, pipeline_name):

        self.execution_id = str(uuid.uuid4())

        self.pipeline_name = pipeline_name

        self.start_time = datetime.now()

        self.end_time = None

        self.status = "RUNNING"

        self.records_read = 0

        self.records_written = 0

        self.records_rejected = 0

    def complete(self, status):

        self.end_time = datetime.now()

        self.status = status