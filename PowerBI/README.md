There are two files:
    - AirQualityUkraine.pbix;
    - LatestData.ptix.

## AirQualityUkraine.pbix
I created this report from a table with fewer columns just to make sure that I can connect to the database and that the data is being loaded correctly

## LatestData.ptix
Let's get the latest data from the Database.

Power BI is primarily designed for visualizing static or historical data rather than real-time data. By default, Power BI does not support automatic real-time data refresh every second. However, there are a few workarounds you can explore to achieve a near-real-time experience:

1. Use DirectQuery
2. Use a Streaming Data Source.
3. Use Power Automate.

I choose first option - DirectQuery:
    Instead of importing data into Power BI, you can connect to your SQL Server database using the DirectQuery mode. DirectQuery allows Power BI to query the database directly each time a report or visualization is refreshed. This way, any updates made to the underlying data in the database will be reflected in the report. However, note that DirectQuery has its own limitations and may impact performance, depending on the complexity and size of your dataset.

It's important to note that achieving true real-time data updates every second in Power BI may not be feasible due to technical limitations and performance considerations. Power BI is optimized for analyzing and visualizing aggregated data rather than processing high-frequency updates. Consider the nature of your data and the desired user experience to determine the appropriate approach for near-real-time data visualization in Power BI.

===== This way was failed =====
===== Resolved by preprocessing due SQL Server =====

If the query you're using contains transformations that are not supported in DirectQuery mode, you'll need to switch to Import mode or find an alternative solution. Here are a few suggestions:

1. Import Data: Switch to Import mode in Power BI to import the data from your SQL Server into Power BI. This allows you to use the full capabilities of Power BI's query editor and perform any necessary transformations before visualizing the data. In Import mode, data is loaded into Power BI's memory, enabling more flexibility in terms of query transformations and aggregations.

2. Materialized View or Summary Table: Consider creating a materialized view or summary table in your SQL Server database that contains the aggregated or transformed data you need for visualization. You can create a separate process or script that populates and updates this table periodically based on your data update frequency. Power BI can then connect to this materialized view or summary table in DirectQuery mode without the need for complex transformations.

3. Stored Procedures: Create a stored procedure in your SQL Server database that performs the necessary query and transformations. Power BI can then execute the stored procedure using DirectQuery mode, retrieving the transformed data directly from the database. You can configure Power BI to execute the stored procedure and visualize the results.

These alternatives provide more flexibility in performing complex transformations and aggregations on your data while still allowing you to connect to your SQL Server database. Evaluate the trade-offs between Import mode, materialized views/summary tables, and stored procedures based on your specific requirements, data volume, and performance considerations.

I choose "Stored Procedures".
You find out query `PROCEDURE_LatestData.sql` in folder `SQL`. Run it in your Database. After that from folder `PowerBI` you can open file `LatestData.pbix`, there i already set up all necessary configuration. But if you want to connect to the stored procedure yourself, then follow these steps:
To use the stored procedure in Power BI:
    1. Go to the "Home" tab and click on "Get Data" or "Get Data > SQL Server" to connect to your SQL Server database.
    2. In the "SQL Server database" window, enter the server name, database name, and choose the "DirectQuery" or "Import" mode.
    3. Click on the "Advanced options" link.
    4. In the "SQL statement" field, enter the following SQL statement to execute the stored procedure:
        `EXEC ProcedureName`
    Replace ProcedureName with the name you provided when creating the stored procedure.
    5. Click on "OK" and follow the prompts to load the data into Power BI.

Now you can use the stored procedure as a data source in Power BI and create visualizations based on the results.
