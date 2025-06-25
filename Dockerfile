# Start from the official Apache Superset image
FROM apache/superset:latest

# Set environment variables
ENV SUPERSET_ENV=production
ENV PYTHONPATH=/app/pythonpath
ENV SUPERSET_CONFIG_PATH=/app/pythonpath/superset_config.py

# Create pythonpath directory
RUN mkdir -p /app/pythonpath

# Copy configuration file
COPY superset_config.py /app/pythonpath/superset_config.py

# Copy bootstrap script
COPY bootstrap.sh /app/bootstrap.sh

# Default port
EXPOSE 8088

# Start Superset
CMD ["/app/bootstrap.sh"]