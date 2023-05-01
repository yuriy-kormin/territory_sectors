from django.conf import settings
from django.views.generic import View
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from .models import Sector
from .PdfGen.process_response import make_response
import os

font_path = os.path.join(
    settings.BASE_DIR,
    'territory_sectors',
    'sector',
    'PdfGen',
    'font',
    'arial.ttf'
)
pdfmetrics.registerFont(TTFont('Arial', font_path))
# pdfmetrics.registerFont(TTFont('TimesCyr', 'times.ttf'))

class SectorPrintPDF(View):
    def get(self, request, pk):
        sector = Sector.objects.get(pk=pk)
        return make_response(request, sector)
