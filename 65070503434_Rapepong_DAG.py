from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
# import sys
# sys.path.append("/home/65070503434_DAG/")

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 26),
    'retries': 1,
}

# Define DAG
with DAG(
    '65070503434_Rapepong_DAG',
    default_args=default_args,
    schedule_interval='0 0 * * *', 
    catchup=False,
    tags=['example'],
) as dag:

    # Start Task (Dummy Operator)
    start = EmptyOperator(task_id='start')

    # Task 1: BashOperator - Prints message
    task_1 = BashOperator(
        task_id='test_directory',
        bash_command='pwd'
    )

    # Task 2: BashOperator - Another Bash command
    task_2 = BashOperator(
        task_id='load_data',
        bash_command='curl http://fastdata.in.th:8000/api/public/dl/ECUJBUIB/65070503434_DAG/train.csv'
        # bash_command='python /home/65070503434_DAG/feature_extraction.py'
    )
    
    # Task 2: BashOperator - Another Bash command
    task_3 = BashOperator(
        task_id='check_data',
        bash_command='ls'
        # bash_command='python /home/65070503434_DAG/feature_extraction.py'
    )

    # End Task (Dummy Operator)
    end = EmptyOperator(task_id='end')

    # Define task dependencies
    start >> task_1 >> task_2 >> task_3 >> end
