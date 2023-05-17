IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.WeatherData') AND type in (N'U'))
BEGIN
    CREATE TABLE WeatherData (
        [id] INT IDENTITY(1,1) NOT NULL,
        [city] VARCHAR(255) NOT NULL,
        [temperature] FLOAT NOT NULL,
        [humidity] INT NOT NULL,
        [wind_speed] FLOAT NOT NULL,
        [weather_description] VARCHAR(255) NOT NULL,
        [timestamp] DATETIME NOT NULL DEFAULT(GETDATE()),
        CONSTRAINT [PK_WeatherData] PRIMARY KEY CLUSTERED 
        (
            [id] ASC
        )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
    ) ON [PRIMARY];
END;
