#!/bin/bash
set -e

echo "Starting Superset bootstrap process..."

# Wait for database to be ready (useful for Render's managed databases)
if [ -n "$DATABASE_URL" ]; then
    echo "Waiting for database to be ready..."
    sleep 5
fi

# Initialize Superset DB
echo "Initializing Superset database..."
superset db upgrade

# Create admin user if not exists
echo "Creating admin user..."
superset fab create-admin \
    --username ${SUPERSET_ADMIN_USERNAME:-admin} \
    --firstname ${SUPERSET_ADMIN_FIRSTNAME:-Superset} \
    --lastname ${SUPERSET_ADMIN_LASTNAME:-Admin} \
    --email ${SUPERSET_ADMIN_EMAIL:-admin@superset.com} \
    --password ${SUPERSET_ADMIN_PASSWORD:-admin} || true

# Load default roles and permissions
echo "Initializing Superset..."
superset init

# Start the server
echo "Starting Superset server on port ${PORT:-8088}..."
exec superset run -h 0.0.0.0 -p ${PORT:-8088} --with-threads --reload --debugger 