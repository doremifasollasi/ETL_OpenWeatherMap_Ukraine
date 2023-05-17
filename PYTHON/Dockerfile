# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Upgrade pip and setuptools
RUN pip install --no-cache-dir --upgrade pip setuptools

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Apache Airflow
RUN pip install --no-cache-dir apache-airflow

# Create the DAGs, plugins, and logs directories
RUN mkdir dags plugins logs

# # Copy the DAGs, plugins, and logs files
# COPY dags/ /app/dags/
# COPY plugins/ /app/plugins/
# COPY logs/ /app/logs/

# Copy the .env file
COPY .env /app/.env

# Set the environment variables
ENV AIRFLOW_HOME="/app"
ENV PYTHONPATH="${PYTHONPATH}:${AIRFLOW_HOME}"
ENV AIRFLOW_ADMIN_PASSWORD=my_password


# Initialize the Airflow database
RUN airflow db init

# Create an Airflow admin user
RUN airflow users create \
    --username admin \
    --firstname Olena \
    --lastname Liahovych \
    --role Admin \
    --email lena.lenova.2014@gmail.com \
    --password ${AIRFLOW_ADMIN_PASSWORD}

# Expose the necessary ports
EXPOSE 8080

# Start the Airflow scheduler and webserver
CMD ["bash", "-c", "airflow scheduler -D & airflow webserver"]
