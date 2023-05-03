#Overview
File `from_openaq_to_sql.py`
- script for retrieving data from the OpenAQ API using Python and pandas, and then loading it into a SQL Server table (how to config SQL Server look at the README file in the SQL folder).

#Settings
##For connection to DB we need few credentials.
A common approach is to store sensitive information in a separate configuration file that is not tracked by version control and is only accessible to authorized users. This file can be read by your code at runtime and used to set up the necessary database connections.

One popular way to manage configuration files in Python projects is to use the `python-dotenv` package. This package allows you to define environment variables in a `.env` file, which can be loaded into your Python script using the `load_dotenv` function.

Here's an example of how you can use `python-dotenv` to store database credentials in a `.env` file and load them into your Python script:

1. Create a file `.env` in the root directory of your project 
2. Add the following contents. But! There are two scenario

2.1. If you are using Windows Authentication to connect to SQL Server (like me), you don't need to provide a password for the `dbo` user. The `dbo` user is the default database owner, and it is usually mapped to the Windows account used to install and configure SQL Server. 
Just add to `.env` next:
DB_SERVER=your_server_name
DB_NAME=your_database_name

2.2. If you create a special user with password, then add to `.env` next:
    DB_SERVER=myserver
    DB_NAME=mydatabase
    DB_USERNAME=myusername
    DB_PASSWORD=mypassword

Then in `from_openaq_to_sql.py` the get database credentials from environment variables:
    `server = os.environ.get("SERVER")`
    `database = os.environ.get("DATABASE")`
    `username = os.environ.get("USERNAME")`
    `password = os.environ.get("PASSWORD")`
Next - Set up the ODBC connection:
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};DATABASE={database};UID={username};PWD={password};"
    )


##Also, make sure you have the necessary libraries installed. For this just running:
`pip install -r requirements.txt`

#More details about `from_openaq_to_sql.py`
The script makes a GET request to the OpenAQ API, specifying the country parameter as 'UA' for Ukraine and the limit parameter as the desired number of records to retrieve. It retrieves the response data as JSON and converts it to a pandas DataFrame. Then, it establishes a connection to SQL Server using pyodbc and writes the data from the DataFrame to the specified table using the to_sql method.

For the future, it is possible to expand the functionality - Make sure to adjust the code according to your specific requirements and API response structure. You may need to map the JSON data fields to the corresponding table columns in order to ensure proper data insertion.

Let me know if you have any further questions!