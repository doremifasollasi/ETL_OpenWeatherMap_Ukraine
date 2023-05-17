FROM mcr.microsoft.com/mssql/server:2019-latest

# Set environment variables
ENV ACCEPT_EULA=Y

# Copy SQL script files
COPY . /docker-entrypoint-initdb.d/

# Copy entrypoint script
COPY entrypoint.sh /usr/src/app/entrypoint.sh

# Copy entrypoint script and set execute permission
COPY --chmod=+x entrypoint.sh /usr/src/app/entrypoint.sh

# Expose port (optional)
EXPOSE 1433

# Start SQL Server
# CMD ["/opt/mssql/bin/sqlservr"]

# Start SQL Server and execute scripts
CMD /usr/src/app/entrypoint.sh
