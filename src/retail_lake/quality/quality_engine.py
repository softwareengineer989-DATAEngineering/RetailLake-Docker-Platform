from retail_lake.quality.quality_rules import(
check_nulls,

check_duplicate
)

from retail_lake.quality.quality_report import QualityReport

class DataQualityEngine:

    def run(self, df):
        
        report = QualityReport()

        report.total_records = df.count()

        report.null_records = check_nulls(

            df,

            df.columns
        )

        report.duplicate_records = check_duplicate(df)

        report.valid_records = (

            report.total_records

            - report.null_records

            - report.duplicate_records

        )

        return report