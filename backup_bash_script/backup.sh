#!/bin/bash

# Load environment variables from .env file
set -o allexport
source ../.env
set +o allexport


# Configuration
DATABASE_URL="$DATABASE_URL"
BACKUP_DIR="backups"
ROTATE_COUNT=30
DATABASE_CONTAINER_NAME="pgdatabase"

# Parse database connection settings from DATABASE_URL
export $(python3 -c "import dj_database_url; print('\n'.join(f'DB_{k.upper()}=\"{v}\"' for k, v in dj_database_url.parse('$DATABASE_URL').items()))")

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

POSTGRES_CONTAINER_ID=$(docker container ls -q -f name=$DATABASE_CONTAINER_NAME)
# Get current date and time
CURRENT_DATE=$(date +"%Y-%m-%d_%H-%M-%S")

# Backup database to file
docker exec -t $POSTGRES_CONTAINER_ID pg_dump -U $DB_USER -Fc $DB_NAME > $BACKUP_DIR/$CURRENT_DATE.dump

# Rotate backups
if [ $(ls -1 $BACKUP_DIR/*.dump | wc -l) -gt $ROTATE_COUNT ]; then
  ls -t $BACKUP_DIR/*.dump | tail -n +$(( $ROTATE_COUNT + 1 )) | xargs rm --
fi
