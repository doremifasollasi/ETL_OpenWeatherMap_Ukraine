import pyodbc
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Get the values of the environment variables
server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
driver = os.getenv('SQL_DRIVER')
trusted_connection = os.getenv('SQL_TRUSTED_CONNECTION')

# Define the connection string using the environment variables
conn_str = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};"

# Connect to the database
try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful")
except Exception as e:
    print("Error connecting to database:", e)