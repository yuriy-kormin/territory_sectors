from django.views.generic import View
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from .models import Sector
from .PdfGen.process_response import make_response

# pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))


class SectorPrintPDF(View):
    def get(self, request, pk):
        sector = Sector.objects.get(pk=pk)
        return make_response(request, sector)
