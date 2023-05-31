##To connect to the PostgreSQL server running inside the container, you have a few options for obtaining the client application.

Spoiler: I choose prefer running pgAdmin 4 as a container.
Spoiler-spoiler: I found out that I can specify `pgadmin4` as a service in the docker-compose structure. For now, I stopped at this option, so I deleted the Dockerfile from this folder.

1. pgAdmin: pgAdmin is a popular client application for managing PostgreSQL databases. You can download it for free from the official website: https://www.pgadmin.org/. Choose the version compatible with your operating system, and follow the installation instructions. Once installed, you can launch pgAdmin and create a new server connection using the details I mentioned in the previous response.

2. psql (PostgreSQL command-line client): psql is a command-line client provided by PostgreSQL that allows you to interact with the PostgreSQL server directly from the terminal. If you already have PostgreSQL installed on your machine, you should have the psql client available. To check if psql is installed, open a terminal or command prompt and type psql followed by Enter. If it is installed, you will enter the psql command-line interface. If not, you may need to install PostgreSQL on your machine. Refer to the PostgreSQL documentation or your operating system's package manager for installation instructions.

3. DBeaver: DBeaver is a free, multi-platform database tool that supports various database management systems, including PostgreSQL. You can download it from the official website: https://dbeaver.io/. Choose the version suitable for your operating system, install it, and then configure a new PostgreSQL connection using the connection details mentioned earlier.

Once you have installed and launched the client application, you can provide the necessary connection details, such as host, port, username, and password, to establish a connection to the PostgreSQL server running inside the Docker container.


## Then if you choose pgAdmin 4, you are looking for installation options for pgAdmin 4. Here are a few installation options for pgAdmin 4:

1.1. Container: If you prefer running pgAdmin 4 as a container, you can use Docker to set it up. There are Docker images available for pgAdmin 4 that you can run as a container on your system. You can refer to the official documentation for more information on running pgAdmin 4 in a Docker container: https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html

1.2. macOS: For macOS, you can download the macOS version of pgAdmin 4 from the official website. Visit the following link to download the macOS version: https://www.pgadmin.org/download/pgadmin-4-macos/

1.3. Python: If you have Python installed on your system, you can use pip, the Python package installer, to install pgAdmin 4. Open a terminal or command prompt and run the following command:
    `pip install pgadmin4`
After the installation, you can launch pgAdmin 4 by running the following command:
    `pgadmin4`

1.4. APT: If you are using a Debian-based Linux distribution, such as Ubuntu, you can use the APT package manager to install pgAdmin 4. Open a terminal and run the following commands:
    `sudo apt update`
    `sudo apt install pgadmin4`

1.5. RPM: If you are using a Red Hat-based Linux distribution, such as Fedora or CentOS, you can use the RPM package manager to install pgAdmin 4. Open a terminal and run the following commands:
    `sudo dnf install pgadmin4`

1.6. Source Code: If you prefer building pgAdmin 4 from source code, you can find the source code on the pgAdmin GitHub repository: https://github.com/postgres/pgadmin4

1.7. Windows: For Windows, you can download the Windows version of pgAdmin 4 from the official website. Visit the following link to download the Windows version: https://www.pgadmin.org/download/pgadmin-4-windows/

Choose the installation option that matches your requirements and follow the respective installation instructions to install pgAdmin 4.

## Build and run the Dockerfile for pgadmin:
Navigate to the pgadmin folder in your terminal:
    `cd pgadmin`
Build the Docker image:
    `docker build -t pgadmin-python .`
or I recommend use it:
    `docker build -t pgadmin-python -f Dockerfile . --no-cache`
Run the Docker container if you will not run the docker-compose:
    `docker run -d --name pgadmin-container -p 5050:5050 pgadmin-python`


## Connections for PostgreSQL
The connection details you need to provide in Apache Airflow are for the PostgreSQL server, not for pgAdmin.

When you add a connection in Airflow, you are specifying the details to connect to the PostgreSQL database where your Airflow metadata and other data will be stored. Airflow uses the connection information to interact with the PostgreSQL server.

Here's how you should fill out the fields for the PostgreSQL connection in Airflow:
    - Conn Id: Enter a unique identifier for the connection, e.g., postgres_default.
    - Conn Type: Select "Postgres" from the dropdown menu.
    - Host: Enter the hostname or IP address of your PostgreSQL server. In your case, since you're using Docker Compose, you can enter postgres as the hostname.
    - Schema: (Optional) Enter the default schema to use for the connection.
    - Login: Enter the username for connecting to the PostgreSQL server. In your case, you can use `airflow`.
    - Password: Enter the password for the specified username. In your case, you can use `airflow`.
    - Port: Enter the port number on which the PostgreSQL server is running. The default port for PostgreSQL is 5432.
    - Extra: You can leave this field empty.

By providing these details, Airflow will establish a connection to your PostgreSQL server and use it for storing metadata and other relevant information.

To summarize, you should insert the data about the PostgreSQL server when adding the connection in Airflow, not the pgAdmin details.

## Work with PostgreSQL due pgAdmin
#To correct fill out fields when adding a server registration in pgAdmin 4, you can follow these steps:

1.Open pgAdmin 4 in your web browser `http://localhost:5050/`
Enter login and password, which you identify in docker-compose:
    `your_email@example.com`
    `your_password`

2. Now you can see main page - `http://localhost:5050/browser/`.
In the left-hand panel, expand the `airflow` (if exist, just then i did at the first time I saw `airflow`, all next times - no. If you also don't see - just create new server group - `airflow`) group to view the list of registered servers. It's empty there.

3. Right-click on the `airflow` group server registration and select `Register` and then `Server` from the context menu.

4. In the `Register - Server` dialog that appears, you will see several fields that need to be filled out. Here's how you can correct them:
    General Tab: Provide a name for the server in the "Name" field. This can be any descriptive name you choose.
        `OWM`
    Connection Tab: Ensure you have the correct information for the server connection.
        Host name/address: Enter the hostname or IP address of the server where your PostgreSQL database is running.
            `172.21.0.1` or for example `172.23.0.1` (I found this value in the logs of the pgadmin container)
        Port: Specify the port number on which your PostgreSQL database is listening. The default is usually 5432.
            `5432`
        Maintenance database: Provide the name of the default database that you want to connect to.
            `postgres` (left the value suggested by the system)
        Username: Enter the username to be used for authentication. I specified such a value as in "docker-compose - services:postgres: environment:POSTGRES_USER:"
            `airflow`
        Password: Input the password associated with the provided username. I specified such a value as in "docker-compose - services:postgres: environment:POSTGRES_USER:"
            `airflow`
    SSL Tab (optional): If your PostgreSQL server uses SSL, you can configure the SSL connection settings in this tab.

    SSH Tunnel Tab (optional): If you need to connect to the PostgreSQL server through an SSH tunnel, you can configure the SSH tunnel settings in this tab.

5. After filling out the necessary fields, click the "Save" button to save the server registration.

Make sure to provide accurate and valid information for the connection details to establish a successful connection to the PostgreSQL server. Double-check the hostname, port, database, username, and password to ensure they are correct.

Once you save the server registration, it should appear in the list of servers in pgAdmin 4, and you should be able to connect to it and interact with the databases and objects within it.

##