#!/bin/bash

# Wait for SQL Server to start
sleep 30s

# Execute all SQL files in the directory

#all
# for file in /docker-entrypoint-initdb.d/*.sql; do
#     echo "Executing $file"
#     /opt/mssql-tools/bin/sqlcmd -S localhost -E -d AirQualityUkraine -i "$file"
# done

#one
sql_file="/docker-entrypoint-initdb.d/2.Create_schema_WeatherDataAll.sql"
echo "Executing $sql_file"
/opt/mssql-tools/bin/sqlcmd -S localhost -E -d AirQualityUkraine -i "$sql_file"


# Start SQL Server
/opt/mssql/bin/sqlservr
