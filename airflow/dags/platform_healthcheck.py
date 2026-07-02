from airflow import DAG

from airflow.operators.python import PythonOperator

from datetime import datetime


def health_check():

    print("RetailLake Platform Healthy")


with DAG(

    dag_id="platform_healthcheck",

    start_date=datetime(2025,1,1),

    schedule="@daily",

    catchup=False,

) as dag:

    task = PythonOperator(

        task_id="health_check",

        python_callable=health_check,

    )