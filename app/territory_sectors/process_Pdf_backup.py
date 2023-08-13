## чтобы функция заработала в скрипте
# from territory_sectors.sector.PdfGen import process_Pdf_backup
    ##
    ## 1) установить env DJANGO_SETTINGS_MODULE.
    ## 2) from django.conf import settings
    ## 3) from django.apps import apps
    ## 4) apps.populate(settings.INSTALLED_APPS)
    ##
    ##     заработает импорт модели
    ##     from territory_sectors.sector.models import Sector
    ## 5) руками добавить testserver в settings.ALLOWED_HOSTS
    ## 6) добавить шрифт как в viewPDFprint
import os
import sys
from pathlib import Path

PROJECT_ROOT = os.path.dirname(Path(__file__).resolve().parent)
sys.path.insert(0, PROJECT_ROOT)
from django.test import RequestFactory
from django.conf import settings
from django.apps import apps
from datetime import datetime

apps.populate(settings.INSTALLED_APPS)

from territory_sectors.sector.PdfGen.utils import set_font
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
from territory_sectors.sector.PdfGen.process_response import make_response
#




from territory_sectors.sector.models import Sector
settings.ALLOWED_HOSTS.append('testserver')

# client = Client()
BACKUP_FOLDER = "."

set_font()
request_factory = RequestFactory()
queryset = Sector.objects.all()[:1]

for sector in queryset:
    # request = client.get('/')
    request = request_factory.get('/')
    pdf_response = make_response(request, sector)
    if pdf_response \
            and pdf_response.status_code == 200 \
            and pdf_response['Content-Type'] == 'application/pdf':
        now = datetime.now()
        date_folder = now.strftime("%Y-%m-%d")
        backup_folder = os.path.join(BACKUP_FOLDER, date_folder)

        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        pdf_filename = f"{sector.name}.pdf"
        pdf_path = os.path.join(backup_folder, pdf_filename)

        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)

        print(f"Generated and saved PDF backup for instance {sector.name}.")
