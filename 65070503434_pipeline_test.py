from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Rapepong',
    'start_date': datetime(2022, 7, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'email': 'admin@bigdata.org',
    'retries': 3,
    'retry_delay': timedelta(seconds=5)
}

with DAG(dag_id='pipeline_test_rapepong', schedule_interval='0 0 * * *', 
    default_args=default_args, catchup=False, tags=["Rapepong","test"]) as dag:

    start = EmptyOperator(task_id="start")

    end = EmptyOperator(task_id="end")

start >> end
