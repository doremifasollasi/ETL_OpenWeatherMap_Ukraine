"""
Python script for retrieving data from the OpenAQ API and loading it into the SQL Server database
"""

import pandas as pd
import pyodbc

# Define the connection details for SQL Server
server = 'localhost'
database = 'MyDatabaseName'
username = 'MyUsername'
password = 'MyPassword'

# Establish a connection to SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Define the API endpoint URL and any required parameters
url = 'https://api.openaq.org/v1/measurements'
parameters = {
    'country': 'UA',  # Set the country parameter to 'UA' for Ukraine
    'limit': 1000     # Set the limit parameter to the desired number of records to retrieve
}

# Make a GET request to the API and retrieve the data as JSON
response = requests.get(url, params=parameters)
data = response.json()

# Convert the JSON data to a pandas DataFrame
df = pd.DataFrame(data['results'])

# Define the SQL Server table name
table_name = 'AirQualityData'

# Write the data from the DataFrame to the SQL Server table
df.to_sql(table_name, conn, if_exists='append', index=False)

# Close the database connection
conn.close()
