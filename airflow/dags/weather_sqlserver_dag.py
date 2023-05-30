import pandas as pd
import pyodbc
import requests
import json
from auxiliary.ukrainian_cities import list_ukrainian_cities
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable


server = Variable.get("SQL_SERVER")
database = Variable.get("SQL_DATABASE")
driver = Variable.get("SQL_DRIVER")
trusted_connection = Variable.get("SQL_TRUSTED_CONNECTION")
user = Variable.get("SQL_USERNAME")
password = Variable.get("SQL_PASSWORD")
owm_api_key = Variable.get("OWM_API_KEY")

# Set up connection string
if trusted_connection.lower() == "yes":
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=;"
else:
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};"

def store_weather_data():
    # Connect to database
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()

    # Load schema definition from schema_table_WeatherData.json
    with open('SCHEMAS/schema_table_WeatherData.json') as f:
        schema = json.load(f)

    # Define the OpenWeatherMap API endpoint URL and any required parameters
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': owm_api_key,  # Your OpenWeatherMap API key
        'units': 'metric',  # Set the units parameter to 'metric' for Celsius
        'lang': 'en'  # Set the language parameter to 'en' for English
    }

    # Define the list of cities in Ukraine to retrieve weather data for
    cities = list_ukrainian_cities

    # Create an empty DataFrame to store the weather data
    df_weather = pd.DataFrame()

    # Loop through each city and retrieve the weather data
    for city in cities:
        params['q'] = city  # Set the 'q' parameter to the current city
        response = requests.get(url, params=params)  # Make a GET request to the API
        data = response.json()  # Parse the JSON data

        # Extract the relevant fields from the JSON data and add them to the DataFrame
        row = {
            'city': city,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'weather_description': data['weather'][0]['description']
        }
        df_weather = pd.concat([df_weather, pd.DataFrame([row])], ignore_index=True)

    # Define the SQL Server table name and schema
    schema_name = 'dbo'
    table_name = 'WeatherData'

    # Store the weather data in the database
    for index, row in df_weather.iterrows():
        # Build the SQL query using the schema definition
        query = f"INSERT INTO {schema_name}.{table_name} (city, temperature, humidity, wind_speed, weather_description) VALUES (?, ?, ?, ?, ?)"

        # Execute the query with the row data as parameters
        cursor.execute(query, row['city'], row['temperature'], row['humidity'], row['wind_speed'], row['weather_description'])
        # Commit the changes to the database
        cnxn.commit()

    print("Weather data successfully saved to the database!")

# Define the DAG
dag = DAG(
    dag_id='weather_sqlserver_dag',
    start_date=datetime(2023, 5, 1),
    schedule_interval='0 0 * * *',
    tags=["olena"]
)

# Define the PythonOperator
store_weather_data_task = PythonOperator(
    task_id='store_weather_data',
    python_callable=store_weather_data,
    dag=dag
)

# Set task dependencies
store_weather_data_task
