import pandas as pd
import pyodbc
import requests
import os
import json
from ukrainian_cities import list_ukrainian_cities


from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
owm_api_key = os.getenv("OWM_API_KEY")

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
df_weather_api = pd.DataFrame()

# Loop through each city and retrieve the weather data
for city in cities:
    params['q'] = city  # Set the 'q' parameter to the current city
    response = requests.get(url, params=params)  # Make a GET request to the API
    data = response.json()  # Parse the JSON data
    
    # Extract the relevant fields from the JSON data and add them to the DataFrame
    rows = {
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

    df_weather_api = pd.concat([df_weather_api, pd.DataFrame([rows])], ignore_index=True)

print('Attributes are defined')

if __name__ == "__main__":
    print(len(rows))
    # Print the list of fields
    for row in rows:
        print(row)