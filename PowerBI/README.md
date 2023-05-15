Power BI is primarily designed for visualizing static or historical data rather than real-time data. By default, Power BI does not support automatic real-time data refresh every second. However, there are a few workarounds you can explore to achieve a near-real-time experience:

1. Use DirectQuery
2. Use a Streaming Data Source.
3. Use Power Automate.

I choose first option - DirectQuery:
    Instead of importing data into Power BI, you can connect to your SQL Server database using the DirectQuery mode. DirectQuery allows Power BI to query the database directly each time a report or visualization is refreshed. This way, any updates made to the underlying data in the database will be reflected in the report. However, note that DirectQuery has its own limitations and may impact performance, depending on the complexity and size of your dataset.

It's important to note that achieving true real-time data updates every second in Power BI may not be feasible due to technical limitations and performance considerations. Power BI is optimized for analyzing and visualizing aggregated data rather than processing high-frequency updates. Consider the nature of your data and the desired user experience to determine the appropriate approach for near-real-time data visualization in Power BI.

