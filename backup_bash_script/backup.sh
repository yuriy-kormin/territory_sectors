#!/bin/bash
# Get the absolute path of the directory that contains the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Load environment variables from .env file
set -o allexport
source "${SCRIPT_DIR}/../.env-compose"
set +o allexport

# Get current date and time
CURRENT_DATE=$(date +"%Y-%m-%d")

# Configuration
DATABASE_URL="$DATABASE_URL"
BACKUP_DIR="backups"
FOLDER_TO_BACKUP="territory_sectors/app/media"
ROTATE_COUNT=30
DATABASE_CONTAINER_NAME="pgdatabase"

# Parse database connection settings from DATABASE_URL
export $(python3 -c "import dj_database_url; print('\n'.join(f'DB_{k.upper()}={v}' for k, v in dj_database_url.parse('$DATABASE_URL').items()))")

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR/$CURRENT_DATE
zip -r "$BACKUP_DIR/$CURRENT_DATE/app" "$FOLDER_TO_BACKUP"

POSTGRES_CONTAINER_ID=$(docker container ls -q -f name=$DATABASE_CONTAINER_NAME)

# Backup database to filecd ..
docker exec -t $POSTGRES_CONTAINER_ID pg_dump -U $DB_USER -d $DB_NAME > $BACKUP_DIR/$CURRENT_DATE/$CURRENT_DATE.dump

# Rotate backups
if [ $(ls -1 $BACKUP_DIR/* | wc -l) -gt $ROTATE_COUNT ]; then
  ls -t $BACKUP_DIR/* | tail -n +$(( $ROTATE_COUNT + 1 ))
  ls -t $BACKUP_DIR/* | tail -n +$(( $ROTATE_COUNT + 1 )) | xargs rm -r --
fi
