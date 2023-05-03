import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# define connection string
conn_str = (
    "Driver={SQL Server};"
    f"Server={os.getenv('DB_SERVER')};"
    f"Database={os.getenv('DB_NAME')};"
    "Trusted_Connection=yes;"
)

# connect to SQL Server
cnxn = pyodbc.connect(conn_str)

# read data from OpenAQ API into a pandas DataFrame
url = "https://api.openaq.org/v1/measurements?country=UA"
df = pd.read_json(url)

# write data to SQL Server table
table_name = "openaq_measurements"
df.to_sql(table_name, cnxn, if_exists="append", index=False)

# close the connection
cnxn.close()
