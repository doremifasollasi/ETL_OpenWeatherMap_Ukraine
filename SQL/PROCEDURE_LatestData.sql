--SELECT wd.*
--FROM WeatherData wd
--INNER JOIN (
--    SELECT [city], max([timestamp]) AS max_timestamp
--    FROM WeatherData
--    GROUP BY [city]
--) t ON wd.[city] = t.[city] AND wd.[timestamp] = t.max_timestamp;

--SELECT wd.*
--FROM WeatherData wd
--WHERE wd.timestamp = (
--    SELECT MAX(timestamp)
--    FROM WeatherData
--    WHERE city = wd.city
--)

CREATE PROCEDURE LatestData
AS
BEGIN
    -- SQL statements and logic for the stored procedure
    -- Replace this with your own query
    SELECT wd.*
    FROM WeatherData AS wd
    INNER JOIN (
        SELECT [city], MAX([timestamp]) AS max_timestamp
        FROM WeatherData
        GROUP BY [city]
    ) AS t ON wd.[city] = t.[city] AND wd.[timestamp] = t.max_timestamp
END;

--DROP PROCEDURE [dbo].[ProcedureName];
