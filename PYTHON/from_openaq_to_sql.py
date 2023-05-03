import pandas as pd
import pyodbc
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
driver = os.getenv("SQL_DRIVER")
trusted_connection = os.getenv("SQL_TRUSTED_CONNECTION")

# Set up connection string
if trusted_connection.lower() == "yes":
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
else:
    user = os.getenv("SQL_USER")
    password = os.getenv("SQL_PASSWORD")
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};"

# Connect to database
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()

# Read data from API using pandas
url = "https://api.openaq.org/v1/measurements"
params = {"country": "UA", "limit": 10000}
response = pd.read_json(url, params=params)
data = response["results"]

# Write data to database
for row in data:
    sql = f"INSERT INTO openaq(country, city, location, parameter, value, unit, date_utc) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, row["country"], row["city"], row["location"], row["parameter"], row["value"], row["unit"], row["date"]["utc"])
cnxn.commit()

# Close database connection
cursor.close()
cnxn.close()
