FROM apache/airflow:2.2.3

# Copy the SCHEMAS folder into the container
COPY SCHEMAS /opt/airflow/SCHEMAS

# Copy files into the container
COPY airflow/requirements.txt /opt/airflow/requirements.txt
COPY airflow/sqlsrv32.dll /opt/airflow/drivers/sqlsrv32.dll

# Install the required packages
RUN pip install -r /opt/airflow/requirements.txt

# Set the working directory
WORKDIR /opt/airflow

# Set the environment variable to use the modified configuration
# Declaring environment variables in a Dockerfile sets static values that are baked into the image.
ENV AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/dags
ENV AIRFLOW__CORE__LOGS_FOLDER=/opt/airflow/logs
ENV AIRFLOW__CORE__PLUGINS_FOLDER=/opt/airflow/plugins

# Initialize the Airflow database
RUN airflow db init