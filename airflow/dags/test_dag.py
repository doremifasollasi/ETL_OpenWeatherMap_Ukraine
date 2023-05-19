from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
from datetime import datetime

def task1():
    # Use SQLite connection
    sqlite_hook = SqliteHook(sqlite_conn_id='sqlite')
    # Perform task using SQLite connection

def task2():
    # Use PostgreSQL connection
    postgres_hook = PostgresHook(postgres_conn_id='postgres')
    # Perform task using PostgreSQL connection

def task3():
    # Use SQL Server connection
    sqlserver_hook = MsSqlHook(mssql_conn_id='sqlserver')
    # Perform task using SQL Server connection

with DAG('test_dag', start_date=datetime(2023, 5, 1), schedule_interval='@daily', tags=["olena"]) as dag:
    t1 = PythonOperator(task_id='task1', python_callable=task1)
    t2 = PythonOperator(task_id='task2', python_callable=task2)
    t3 = PythonOperator(task_id='task3', python_callable=task3)

    t1 >> t2 >> t3
