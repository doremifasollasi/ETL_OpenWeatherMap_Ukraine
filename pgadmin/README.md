##To connect to the PostgreSQL server running inside the container, you have a few options for obtaining the client application.

Spoiler: I choose prefer running pgAdmin 4 as a container

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

## To build and run the Dockerfiles for both pgadmin and airflow, and then run docker-compose, you can follow these steps:
1. Build and run the Dockerfile for pgadmin:
Navigate to the pgadmin folder in your terminal:
    `cd pgadmin`
Build the Docker image:
    `docker build -t pgadmin-image .`
    `docker build -t pgadmin-python -f Dockerfile . --no-cache`
Run the Docker container if you will not run the docker-compose:
    `docker run -d --name pgadmin-container -p 5050:5050 pgadmin-image`
