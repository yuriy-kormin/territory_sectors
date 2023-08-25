#!/bin/bash
## To correctly run this script, you need to install several tools
##
## jq  #pasrse json data
## zip
##  rclone (to upload backups to clouds)
##

# Configuration
BACKUP_DIR="backups"
FOLDER_TO_BACKUP="territory_sectors/app/media"
FOLDER_WITH_PDFS="territory_sectors/backup"
ROTATE_COUNT=15
DATABASE_CONTAINER_NAME="pgdatabase"
DJANGO_CONTAINER_NAME="sectors-sectors"
REMOTE_NAME="batum"  # The name of the remote configured in rclone
REMOTE_STORE_FOLDER="backup_sectors"  # The name of the remote folder in rclone
REMOTE_ROTATE_COUNT=3 # Count of the remote backups stored

# Get the absolute path of the directory that contains the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Load environment variables from .env file
set -o allexport
source "${SCRIPT_DIR}/../.env-compose"
set +o allexport

# Get current date and time
CURRENT_DATE=$(date +"%Y-%m-%d")

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR/$CURRENT_DATE
zip -r "$BACKUP_DIR/$CURRENT_DATE/media" "$FOLDER_TO_BACKUP"

POSTGRES_CONTAINER_ID=$(docker container ls -q -f name=$DATABASE_CONTAINER_NAME)
DJANGO_CONTAINER_ID=$(docker container ls -q -f name=$DJANGO_CONTAINER_NAME)

# Backup database to filecd ..
docker exec -t $POSTGRES_CONTAINER_ID pg_dump -U $POSTGRES_USER -d $POSTGRES_DB > $BACKUP_DIR/$CURRENT_DATE/$CURRENT_DATE.dump

#backup pdfs with sectors
docker exec $DJANGO_CONTAINER_ID bash -c "export DJANGO_SETTINGS_MODULE='territory_sectors.settings' && cd /app && python3 territory_sectors/process_Pdf_backup.py"

# zip result
zip -r "$BACKUP_DIR/$CURRENT_DATE/pdf" "$FOLDER_WITH_PDFS"

# Rotate backups
if [ $(ls -1 $BACKUP_DIR | wc -l) -gt $ROTATE_COUNT ]; then
  ls -t $BACKUP_DIR | tail -n +$(( $ROTATE_COUNT + 1 ))
  ls -t $BACKUP_DIR | tail -n +$(( $ROTATE_COUNT + 1 )) | xargs rm -r --
fi

####################################
####   UPLOAD TO REMOTE CLOUD   ####
####################################
echo "upload to remote"
rclone copy $BACKUP_DIR/$CURRENT_DATE $REMOTE_NAME:$REMOTE_STORE_FOLDER/$CURRENT_DATE


# Retrieve the remote folder contents and store it in a JSON file
rclone lsjson $REMOTE_NAME:$REMOTE_STORE_FOLDER > remote_contents.json

# Extract folder names (dates) and modification times from the JSON file
folders_and_dates=$(jq -r '.[] | select(.IsDir) | "\(.Name) \(.ModTime)"' remote_contents.json)

# Sort folders by date (modification time)
sorted_folders_and_dates=$(echo "$folders_and_dates" | sort -k 2 -r)

# Extract the folder names from the sorted list
sorted_folders=$(echo "$sorted_folders_and_dates" | cut -d ' ' -f 1)

# Calculate the number of folders to keep
keep_count=$(($(echo "$sorted_folders" | wc -l) - $REMOTE_ROTATE_COUNT))

# Extract the folders to delete
folders_to_delete=$(echo "$sorted_folders" | head -n $keep_count)

# Loop through and delete folders
for folder in $folders_to_delete; do
    echo "remove ${REMOTE_NAME}:${REMOTE_STORE_FOLDER}/${folder}"
    rclone purge $REMOTE_NAME:$REMOTE_STORE_FOLDER/$folder
done

# Remove the temporary JSON file
rm remote_contents.json






