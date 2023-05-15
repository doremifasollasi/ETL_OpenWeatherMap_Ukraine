#Overview
File `from_owm_to_sql.py`
- script for retrieving data from the OpenWeatherMap API using Python and pandas, and then loading it into a SQL Server table (how to config SQL Server look at the README file in the SQL folder).

#Settings
##For connection to DB we need few credentials.
A common approach is to store sensitive information in a separate configuration file that is not tracked by version control and is only accessible to authorized users. This file can be read by your code at runtime and used to set up the necessary database connections.

One popular way to manage configuration files in Python projects is to use the `python-dotenv` package. This package allows you to define environment variables in a `.env` file, which can be loaded into your Python script using the `load_dotenv` function.

Here's an example of how you can use `python-dotenv` to store database credentials in a `.env` file and load them into your Python script:

1. Create a file `.env` in the root!!! directory of your project. 
2. Add the following contents to `.env`:
    SQL_SERVER=your_server_name
    SQL_DATABASE=your_database_name
    SQL_DRIVER=your_server_name
    SQL_TRUSTED_CONNECTION=yes_or_no*
    **

*As for the SQL_TRUSTED_CONNECTION value, this should be set to `yes` if you are using Windows authentication, and `no` if you are using SQL Server authentication.
**If you're using SQL Server authentication include in the  file `.env`
    SQL_USERNAME=your_username
    SQL_PASSWORD=your_password

##Connection to OpenWeatherMap API.
To get the weather information for all regional centers of Ukraine, you will need to make a call to the OpenWeatherMap API for each city. One way to do this is to create a list of the cities you are interested in, and then iterate over the list, making a call to the API for each city.

So, for OpenWeatherMap API, you can follow these steps:

1. Go to the OpenWeatherMap website and sign up for a free API key.
2. Once you have the API key, you can make requests to the API using the requests module in Python.
3. To get weather data for a specific location, you can use the "Current weather data" API endpoint. The endpoint URL is "https://api.openweathermap.org/data/2.5/weather". You will need to pass your API key as a parameter, along with the location you want to get weather data for.
    3.1. Add the following contents to `.env`:
    OWM_API_KEY=Replace_this_with_YOUR_API_KEY

4. The API returns the weather data in JSON format. You can use the json module in Python to parse the JSON data and extract the information you need.

##Use `init.bat` file for automate 
- sets up a virtual environment, 
- installs the necessary Python packages, 
- and runs a specific Python script for OpenWeatherMap data conversion and storage in a SQL database.. For this just running from root:
    `init.bat PYTHON\my_script.py`

#More details about `from_owm_to_sql.py`
The script makes a GET request to the OpenWeatherMap API, specifying the country parameter as 'UA' for Ukraine and the limit parameter as the desired number of records to retrieve. It retrieves the response data as JSON and converts it to a pandas DataFrame. Then, it establishes a connection to SQL Server using pyodbc and writes the data from the DataFrame to the specified table using the to_sql method.

For the future, it is possible to expand the functionality - Make sure to adjust the code according to your specific requirements and API response structure. You may need to map the JSON data fields to the corresponding table columns in order to ensure proper data insertion.

Let me know if you have any further questions!

#Explain every row.Let's go through Python script step by step:
1. Import the necessary libraries:
    - pandas: Used for data manipulation and analysis.
    - pyodbc: Provides Python connectivity to SQL Server databases.
    - requests: Used to send HTTP requests and retrieve data from APIs.
    - dotenv: Helps load environment variables from a .env file.
    - os: Provides a way to access operating system functionality.
    - json: Used to work with JSON data.
    - list_ukrainian_cities: Used for code flexibility so as not to be hardcoded. 
2. Load environment variables from a .env file using load_dotenv().
3. Retrieve environment variables using os.getenv() for the SQL Server connection details (server, database, driver, trusted_connection) and the OpenWeatherMap API key (owm_api_key).
4. Set up the connection string based on the trusted_connection variable. If trusted connection is enabled, the connection string is built without a username and password. Otherwise, the username and password are also included in the connection string.
5. Connect to the SQL Server database using pyodbc.connect(). This establishes a connection and returns a connection object (cnxn), which is used to interact with the database.
6. Load the schema definition from the schema_table_WeatherData.json file using json.load() and assign it to the schema variable. This schema definition likely contains information about the table structure.
7. Define the OpenWeatherMap API endpoint URL (url) and the required parameters (params). The parameters include your OpenWeatherMap API key, the units for temperature (Celsius), and the language (English).
8. Define the list of cities in Ukraine for which you want to retrieve weather data. For this import 
9. Create an empty DataFrame (df_weather) to store the weather data.
10. Loop through each city in the cities list.
11. Set the q parameter in the params dictionary to the current city.
12. Make a GET request to the OpenWeatherMap API using requests.get() and passing the URL and parameters.
13. Parse the JSON response using response.json() and assign the resulting data to the data variable.
14 Extract the relevant fields from the data dictionary and create a row dictionary with the city name, temperature, humidity, wind speed, and weather description.
15. Append the row dictionary as a DataFrame row to the df_weather DataFrame using pd.concat().
16. After the loop, the df_weather DataFrame contains weather data for all the cities.
17. Define the SQL Server table name and schema (schema_name and table_name).
18. Iterate over each row in the df_weather DataFrame using df_weather.iterrows().
19. Build the SQL query to insert the weather data into the database using the schema definition. The query is parameterized with placeholders (?) for the values.
20. Execute the query with the row data as parameters using cursor.execute().
21. Commit the changes to the database using cnxn.commit().
22. Print a success message indicating that the weather data has been saved to the database.
23. That's a summary of how your Python script works. It retrieves weather data from the OpenWeatherMap API for a list of cities in Ukraine, stores the data in a DataFrame, and then inserts it into a SQL Server database.
