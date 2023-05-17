IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.WeatherDataAll') AND type in (N'U'))
BEGIN
    CREATE TABLE WeatherDataAll (
        [id] INT IDENTITY(1,1) NOT NULL,
        [city] VARCHAR(255) NOT NULL,
        [temperature] FLOAT NOT NULL,
        [humidity] INT NOT NULL,
        [wind_speed] FLOAT NOT NULL,
        [weather_description] VARCHAR(255) NOT NULL,
        [pressure] FLOAT NOT NULL,
        [visibility] INT NOT NULL,
        [sunrise] INT NOT NULL,
        [sunset] INT NOT NULL,
        [country] VARCHAR(255) NOT NULL,
        [cloudiness] INT NOT NULL,
        [coord_lon] FLOAT NOT NULL,
        [coord_lat] FLOAT NOT NULL,
        [weather_id] INT NOT NULL,
        [weather_main] VARCHAR(255) NOT NULL,
        [timezone] INT NOT NULL,
        [timestamp] DATETIME NOT NULL DEFAULT(GETDATE()),
        CONSTRAINT [PK_WeatherDataAll] PRIMARY KEY CLUSTERED 
        (
            [id] ASC
        )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
    ) ON [PRIMARY];
END;
