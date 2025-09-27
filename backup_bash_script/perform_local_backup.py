import datetime
import subprocess

from conf import BACKUP_DIR, DATABASE_CONTAINER_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, \
    DJANGO_CONTAINER_NAME

FOLDER_TO_BACKUP = "territory_sectors/app/media"
FOLDER_WITH_PDFS = "territory_sectors/backup"

# -------------------
# DATE SETUP
# -------------------
today = datetime.date.today().strftime("%Y-%m-%d")
backup_path = BACKUP_DIR / today
backup_path.mkdir(parents=True, exist_ok=True)

# -------------------
# DATABASE BACKUP
# -------------------
with open(backup_path / f"{today}.dump", "wb") as f:
    subprocess.run([
        "docker", "exec", "-t", DATABASE_CONTAINER_NAME,
        "pg_dump", "-U", DATABASE_USERNAME,
        "-d", DATABASE_PASSWORD
    ], stdout=f, check=True)

# -------------------
# MEDIA BACKUP
# -------------------
subprocess.run(["zip", "-r", str(backup_path / "media.zip"), FOLDER_TO_BACKUP], check=True)

# -------------------
# PDF BACKUP (via Django container)
# -------------------
subprocess.run([
    "docker", "exec", DJANGO_CONTAINER_NAME,
    "bash", "-c",
    "export DJANGO_SETTINGS_MODULE='territory_sectors.settings' && cd /app && python3 territory_sectors/process_Pdf_backup.py"
], check=True)
subprocess.run(["zip", "-r", str(backup_path / "pdfs.zip"), FOLDER_WITH_PDFS], check=True)
