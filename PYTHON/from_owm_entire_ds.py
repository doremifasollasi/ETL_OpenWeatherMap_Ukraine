import pandas as pd
import pyodbc
import requests
import os
import json
from ukrainian_cities import list_ukrainian_cities

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
driver = os.getenv("SQL_DRIVER")
trusted_connection = os.getenv("SQL_TRUSTED_CONNECTION")
owm_api_key = os.getenv("OWM_API_KEY")

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
        'weather_description': data['weather'][0]['description'],
        'pressure': data['main']['pressure'],
        'visibility': data['visibility'],
        'sunrise': data['sys']['sunrise'],
        'sunset': data['sys']['sunset'],
        'country': data['sys']['country'],
        'cloudiness': data['clouds']['all'],
        'coord_lon': data['coord']['lon'],
        'coord_lat': data['coord']['lat'],
        'weather_id': data['weather'][0]['id'],
        'weather_main': data['weather'][0]['main'],
        'timezone': data['timezone']
    }

    df_weather = pd.concat([df_weather, pd.DataFrame([row])], ignore_index=True)

# Define the SQL Server table name and schema
schema_name = 'dbo'
table_name = 'WeatherDataAll'

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
