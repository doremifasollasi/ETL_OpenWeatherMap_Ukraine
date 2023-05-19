REM Build pgadmin container
cd pgadmin
docker build -t pgadmin-python -f Dockerfile . --no-cache

REM Build airflow container
cd ../airflow
docker build -t airflow-sqlserver -f Dockerfile . --no-cache

REM Run docker-compose
cd ..
docker-compose up

@REM Please note that 
@REM I've added cd .. after building the airflow container to move back to the parent directory before running docker-compose up. 
@REM This assumes that the script file is located in the same parent directory as the pgadmin and airflow folders.
