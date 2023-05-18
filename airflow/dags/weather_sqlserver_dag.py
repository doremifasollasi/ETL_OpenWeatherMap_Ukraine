from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from airflow.utils.dates import days_ago

import json

def _process_weather(ti):
    info = ti.xcom_pull("extract_data")
    timestamp = info["dt"]
    temp = info["main"]["temp"]
    return timestamp, temp

with DAG(dag_id="weather_sqlserver_dag", schedule_interval="@hourly", start_date=days_ago(2), catchup=False) as dag:
    db_create = MsSqlOperator(
        task_id="create_weather_table",
        mssql_conn_id="airflow_conn",
        sql="""
            IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='measures')
            CREATE TABLE measures
            (
                timestamp DATETIME,
                temp FLOAT
            );
        """
    )

    check_api = HttpSensor(
        task_id="check_api",
        http_conn_id="weather_conn",
        endpoint="data/2.5/weather",
        request_params={"appid": Variable.get("WEATHER_API_KEY"), "q": "Lviv"}
    )

    extract_data = SimpleHttpOperator(
        task_id="extract_data",
        http_conn_id="weather_conn",
        endpoint="data/2.5/weather",
        data={"appid": Variable.get("WEATHER_API_KEY"), "q": "Lviv"},
        method="GET",
        response_filter=lambda x: json.loads(x.text),
        log_response=True
    )

    process_data = PythonOperator(
        task_id="process_data",
        python_callable=_process_weather
    )

    inject_data = MsSqlOperator(
        task_id="inject_data",
        mssql_conn_id="airflow_conn",
        sql="""
        INSERT INTO measures (timestamp, temp) VALUES ('{{ti.xcom_pull(task_ids="process_data")[0]}}', '{{ti.xcom_pull(task_ids="process_data")[1]}}');
        """,
    )

db_create >> check_api >> extract_data >> process_data >> inject_data
