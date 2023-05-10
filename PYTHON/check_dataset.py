import pandas as pd
import pyodbc
import requests
from dotenv import load_dotenv
import os
import json

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
with open('schema_table_WeatherData.json') as f:
    schema = json.load(f)

# Define the OpenWeatherMap API endpoint URL and any required parameters
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'appid': owm_api_key,  # Your OpenWeatherMap API key
    'units': 'metric',  # Set the units parameter to 'metric' for Celsius
    'lang': 'en'  # Set the language parameter to 'en' for English
}

# Define the list of cities in Ukraine to retrieve weather data for
cities = ['Kyiv', 'Kharkiv', 'Odesa', 'Dnipro', 'Donetsk', 'Zaporizhzhia', 'Lviv', 'Kryvyi Rih', 'Mykolaiv', 'Mariupol', 'Luhansk', 'Vinnytsia', 'Makiivka', 'Simferopol', 'Sevastopol', 'Kherson', 'Poltava', 'Chernihiv', 'Cherkasy', 'Sumy', 'Zhytomyr', 'Khmelnytskyi', 'Rivne', 'Ivano-Frankivsk', 'Kremenchuk', 'Ternopil', 'Lutsk', 'Bila Tserkva', 'Kramatorsk', 'Melitopol', 'Kerch']

# Create an empty DataFrame to store the weather data
df_weather = pd.DataFrame()

# Empty list to store API responses
api_responses = []

# Loop through each city and retrieve the weather data
for city in cities:
    params['q'] = city  # Set the 'q' parameter to the current city
    response = requests.get(url, params=params)  # Make a GET request to the API
    data = response.json()  # Parse the JSON data
        
    # Add the entire API response to the DataFrame
    df_weather = pd.concat([df_weather, pd.json_normalize(data)], ignore_index=True)

    # Append the API response to the list
    api_responses.append(data)

print("Weather Data:")
print(df_weather)

print("\nAPI Responses:")
for response in api_responses:
    print(response)
