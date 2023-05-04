Here's an outline of the steps you can take:

1. Open SQL Server Management Studio (SSMS) and connect to your local instance of SQL Server. Pay attention to how you log in.

2. Create a new database for your project by right-clicking on the "Databases" node in Object Explorer and selecting "New Database". Name the database something relevant to your project, such as "OpenWeatherMapUkraine".

3. Create a new table to store the data from the OpenWeatherMap API. You can use the following SQL query as a starting point:

    file "1.Create_table.sql"

This will create a table called "WeatherData" with columns for the location, parameter, date and time (in UTC), and value of each air quality measurement.

4. Define the schema for your data by specifying the data types for each column in the table. For example, you can use the following SQL commands to set the data types for each column:

    file "2.Create_schema.sql"

5. Once you have created your table and defined the schema, you can start retrieving data from the OpenWeatherMap API and loading it into your database using Python and pandas. You can use the pandas  function to read the data from the API into a DataFrame, and then use the  method to write the data to the SQL Server.

I hope this helps get you started with your ETL project. 
Let me know if you have any further questions!