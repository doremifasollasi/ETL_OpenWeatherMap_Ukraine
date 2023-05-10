-- Change the data types of existing columns
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [city] VARCHAR(255);
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [temperature] FLOAT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [humidity] INT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [wind_speed] FLOAT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [weather_description] VARCHAR(255);
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [pressure] FLOAT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [visibility] INT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [sunrise] INT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [sunset] INT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [country] VARCHAR(255);
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [cloudiness] INT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [coord_lon] DECIMAL(9, 6); -- Change to DECIMAL data type
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [coord_lat] DECIMAL(9, 6); -- Change to DECIMAL data type
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [weather_id] INT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [weather_main] VARCHAR(255);
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [timezone] INT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [id] INT;
ALTER TABLE [dbo].[WeatherDataAll] ALTER COLUMN [timestamp] DATETIME;