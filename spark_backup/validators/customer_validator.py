from pyspark.sql import DataFrame


def validate_customer_data(df: DataFrame):

    count = df.count()

    if count == 0:
        raise Exception("Customer dataframe is empty.")

    print(f"Validation Passed : {count} records")