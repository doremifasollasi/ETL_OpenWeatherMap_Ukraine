from datetime import datetime
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator

def _hello_world():
	logging.info("Hello, World!")

with DAG(dag_id="first_python_dag", schedule_interval="@daily", start_date=datetime(2023, 5, 15), catchup=False) as dag:
	hello_world = PythonOperator(
		task_id="python_task",
		python_callable=_hello_world
	)
