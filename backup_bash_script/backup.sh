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
BACKUP_DIR="backups"
FOLDER_TO_BACKUP="app/territory_sectors/app/media"
ROTATE_COUNT=30
DATABASE_CONTAINER_NAME="pgdatabase"


# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR/$CURRENT_DATE
zip -r "$BACKUP_DIR/$CURRENT_DATE/app" "$FOLDER_TO_BACKUP"

POSTGRES_CONTAINER_ID=$(docker container ls -q -f name=$DATABASE_CONTAINER_NAME)

echo "$POSTGRES_USER"
echo "$POSTGRES_DB"
# Backup database to filecd ..
docker exec -t $POSTGRES_CONTAINER_ID pg_dump -U $POSTGRES_USER -d $POSTGRES_DB > $BACKUP_DIR/$CURRENT_DATE/$CURRENT_DATE.dump

# Rotate backups
if [ $(ls -1 $BACKUP_DIR/* | wc -l) -gt $ROTATE_COUNT ]; then
  ls -t $BACKUP_DIR/* | tail -n +$(( $ROTATE_COUNT + 1 ))
  ls -t $BACKUP_DIR/* | tail -n +$(( $ROTATE_COUNT + 1 )) | xargs rm -r --
fi
