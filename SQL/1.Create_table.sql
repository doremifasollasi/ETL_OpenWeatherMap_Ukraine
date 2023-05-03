CREATE TABLE [dbo].[AirQualityData](
    [id] [bigint] IDENTITY(1,1) NOT NULL,
    [location] [nvarchar](255) NOT NULL,
    [parameter] [nvarchar](50) NOT NULL,
    [date_utc] [datetime] NOT NULL,
    [value] [float] NOT NULL,
 CONSTRAINT [PK_AirQualityData] PRIMARY KEY CLUSTERED 
(
    [id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY];
