#!/bin/bash

# Initialize Superset DB
superset db upgrade

# Create admin user if not exists
superset fab create-admin \
    --username admin \
    --firstname Superset \
    --lastname Admin \
    --email admin@superset.com \
    --password admin || true

# Load default roles and permissions
superset init

# Start the server
superset run -h 0.0.0.0 -p 8088