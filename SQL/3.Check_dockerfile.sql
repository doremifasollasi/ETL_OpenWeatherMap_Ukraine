CREATE TABLE WeatherDataDockerfile (
        [id] INT IDENTITY(1,1) NOT NULL,
        [city] VARCHAR(255) NOT NULL,
        [temperature] FLOAT NOT NULL,
        CONSTRAINT [PK_WeatherDataDockerfile] PRIMARY KEY CLUSTERED 
        (
            [id] ASC
        )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
    ) ON [PRIMARY];

