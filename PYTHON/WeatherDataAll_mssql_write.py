import pandas as pd
import pyodbc
import requests
import os
import json
from ukrainian_cities import list_ukrainian_cities
import WeatherDataAll_owm_read

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Get environment variables
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
driver = os.getenv("SQL_DRIVER")
trusted_connection = os.getenv("SQL_TRUSTED_CONNECTION")

# Set up connection string
if trusted_connection.lower() == "yes":
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=;"
else:
    user = os.getenv("SQL_USER")
    password = os.getenv("SQL_PASSWORD")
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};"

# Connect to database
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()

# Load schema definition from schema_table_WeatherData.json
with open('schema_table_WeatherDataAll.json') as f:
    schema = json.load(f)


# Define the SQL Server table name and schema
schema_name = 'dbo'
table_name = 'WeatherDataAll'

# Create an empty DataFrame to store the weather data
df_weather = WeatherDataAll_owm_read.df_weather_api
print('DataFrame are defined')

# Store the weather data in the database
for index, row in df_weather.iterrows():
    # Build the SQL query using the schema definition
    query = f"INSERT INTO {schema_name}.{table_name} (city, temperature, humidity, wind_speed, weather_description, pressure, visibility, sunrise, sunset, country, cloudiness, coord_lon, coord_lat, weather_id, weather_main, timezone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    # Execute the query with the row data as parameters
    cursor.execute(query, 
                   row['city'], 
                   row['temperature'], 
                   row['humidity'], 
                   row['wind_speed'], 
                   row['weather_description'], 
                   row['pressure'], 
                   row['visibility'], 
                   row['sunrise'], 
                   row['sunset'], 
                   row['country'], 
                   row['cloudiness'], 
                   row['coord_lon'], 
                   row['coord_lat'], 
                   row['weather_id'], 
                   row['weather_main'], 
                   row['timezone'])
  
# Commit the changes to the database
cnxn.commit()
print("Weather data successfully saved to the database!")
