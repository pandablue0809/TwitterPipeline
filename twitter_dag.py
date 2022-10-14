from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl

default_args = {
    'owner': 'airflow',                     # Setting Owner of the Dag.
    'depends_on_past': False,               # Only one Dag, So set False. 
    'start_date': datetime(2020, 11, 8),    # When to start the dag.
    'email': ['airflow@example.com'],       # To get email notification.
    'email_on_failure': False,              # To get email on failure.
    'email_on_retry': False,                # To get email on retry.
    'retries': 1,                           # Number of retry.
    'retry_delay': timedelta(minutes=1)     # delay between each retry.
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='My first etl code',
    schedule_interval=timedelta(days=1)
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag,
)

run_etl
