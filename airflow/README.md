## Build and run the Dockerfile for airflow:
Navigate to the pgadmin folder in your terminal:
    `cd airflow`
Build the Docker image:
    `docker build -t airflow-sqlserver .`
or I recommend use it:
    `docker build -t airflow-sqlserver -f Dockerfile . --no-cache`
Run the Docker container if you will not run the docker-compose:
    `docker run -d --name airflow-container -p 9099:8080 airflow-sqlserver`


## Setup environment
If you want to access the `airflow.cfg` file from the `etl_openweathermap_ukraine-airflow-webserver-1` container, you should copt it. By using the `docker cp` command, you were able to extract it file from the container and make it available on your local machine.

This allows you to inspect the content of the file, make modifications if necessary, or use them as a reference for setting up a similar environment locally. It can be helpful when you need to examine specific configuration files or access data generated or stored within a Docker container.

Overall, the docker cp command provides a convenient way to extract files from Docker containers, enabling you to interact with and analyze the contents of the container from your local machine.
    `cd airflow`
    `docker cp etl_openweathermap_ukraine-airflow-webserver-1:/opt/airflow/airflow.cfg ./airflow.cfg`


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

[4. Connection for work with PostgreSQL](https://github.com/doremifasollasi/ETL_OpenWeatherMap_Ukraine/blob/16cf986f3267820718efc966280f1ecc4459debc/pgadmin/README.md#L50)
