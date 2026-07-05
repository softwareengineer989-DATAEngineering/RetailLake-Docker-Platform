

class QualityReport:

    def __init__(self):
        self.total_records = 0
        self.null_records = 0
        self.duplicate_records = 0
        self.valid_records = 0

    def summary(self):

        return{

            "total_records": self.total_records,

            "null_records": self.null_records,

            "duplicate_records": self.duplicate_records,

            "valid_records": self.valid_records

        }