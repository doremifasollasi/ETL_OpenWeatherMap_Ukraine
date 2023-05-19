## Build and run the Dockerfile for airflow:

Build the Docker image:
    `docker build -t airflow-image .`
or I recommend use it:
    `docker build -t airflow-sqlserver -f airflow/Dockerfile . --no-cache`

Run the Docker container if you will not run the docker-compose:
    `docker run -d --name airflow-container -p 9099:8080 airflow-image`
