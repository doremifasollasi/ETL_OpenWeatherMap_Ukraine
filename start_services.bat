REM Build pgadmin container
docker build -t pgadmin-python -f pgadmin/Dockerfile . --no-cache

REM Build airflow container
docker build -t airflow-sqlserver -f airflow/Dockerfile . --no-cache

REM Run docker-compose
docker-compose up

@REM Please note that 
@REM I've added cd .. after building the airflow container to move back to the parent directory before running docker-compose up. 
@REM This assumes that the script file is located in the same parent directory as the pgadmin and airflow folders.
