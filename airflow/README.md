## Build and run the Dockerfile for airflow:
Navigate to the pgadmin folder in your terminal:
    `cd airflow`
Build the Docker image:
    `docker build -t airflow-sqlserver .`
or I recommend use it:
    `docker build -t airflow-sqlserver -f Dockerfile . --no-cache`
Run the Docker container if you will not run the docker-compose:
    `docker run -d --name airflow-container -p 9099:8080 airflow-sqlserver`

## Connections for few services
The connection details you need to provide in Apache Airflow 
    `http://localhost:9099/connection/list/`. 
For ease of navigation and search, use the description, for example: 
    `For pet project`

1. Connection for work with MSSQLServer
    Id - `weather_conn_sqlserver`
    Type - `MS SQL Server`
    Host - Determine the IP address or hostname of the machine running the SQL Server instance. 
        1.1. You can use tools like: 
            `ipconfig` (Windows) or `ifconfig` (Linux/macOS) 
        to find the IP address. Then choose value from row Wireless LAN adapter - IPv4 Address.
        1.2. Another way - if you have identified the network interface name, you can retrieve the IP address associated with it by using the ipconfig command with the specific network interface name. For example, if the network interface name is "Wi-Fi," you would run the following command:
            `ipconfig /all | findstr "Wi-Fi"`
    Schema - `AirQualityUkraine`
    Login - `airflow`

2. Connection for work with SQLite
    Id - `weather_conn_sqlite`
    Type - `SQLite`
    Host - `sqlite:////container/absolute/path/to/your/airflow.db`

3. Connection for work with HTTP sensor
    Id - `weather_conn_http_sensor`
    Type - `Http`
    Host - `https://api.openweathermap.org`

[## Connections for PostgreSQL](https://github.com/doremifasollasi/ETL_OpenWeatherMap_Ukraine/blob/16cf986f3267820718efc966280f1ecc4459debc/pgadmin/README.md#L50)
