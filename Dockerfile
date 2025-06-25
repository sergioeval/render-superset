# Start from the official Apache Superset image
FROM apache/superset:latest

# Set environment variables
ENV SUPERSET_ENV=production

# Optional: install any extra packages if needed
# RUN pip install --no-cache-dir your-extra-packages

# Superset needs the database to be initialized on first run
COPY docker-bootstrap.sh /app/docker-bootstrap.sh
RUN chmod +x /app/docker-bootstrap.sh

# Default port
EXPOSE 8088

# Start Superset
CMD ["/app/docker-bootstrap.sh"]