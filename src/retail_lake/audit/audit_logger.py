class AuditLogger:

    @staticmethod
    def log(record):

        print()

        print("=" * 70)

        print("PIPELINE AUDIT")

        print("=" * 70)

        print(f"Execution ID    : {record.execution_id}")

        print(f"Pipeline        : {record.pipeline_name}")

        print(f"Status          : {record.status}")

        print(f"Started         : {record.start_time}")

        print(f"Finished        : {record.end_time}")

        print(f"Records Read    : {record.records_read}")

        print(f"Records Written : {record.records_written}")

        print(f"Rejected        : {record.records_rejected}")

        print("=" * 70)

        print()