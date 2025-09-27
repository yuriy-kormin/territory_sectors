import os

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pathlib import Path
from dotenv import load_dotenv


env_path = os.path.join(Path(__file__).resolve().parent.parent, '.env-compose')
load_dotenv(env_path)
BACKUP_DIR = Path("backups")
ROTATE_COUNT = os.getenv("ROTATE_COUNT", "10")
DJANGO_CONTAINER_NAME = "sectors"

DATABASE_CONTAINER_NAME = "pgdatabase"
DATABASE_USERNAME = os.getenv("POSTGRES_USER")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")

folder_id = os.getenv('FOLDER_ID')

settings = {
                "client_config_backend": "service",
                "service_config": {
                    "client_json_file_path": "backup-sectors-data.json",
                }
            }
gauth = GoogleAuth(settings=settings)
gauth.ServiceAuth()
drive = GoogleDrive(gauth)

