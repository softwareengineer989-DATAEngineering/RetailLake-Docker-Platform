from pyspark.sql.functions import col


def check_nulls(df, columns):

    total =  0

    for column in columns:

        total += df.filter(col(column).isNull()).count()

        return total

def check_duplicate(df):

    return df.count() - df.dropDuplicates().count()

