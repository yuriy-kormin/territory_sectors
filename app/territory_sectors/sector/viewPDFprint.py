from django.views.generic import View

from .PdfGen.utils import set_font
from .models import Sector
from .PdfGen.process_response import make_response


class SectorPrintPDF(View):
    def get(self, request, pk):
        set_font()
        sector = Sector.objects.get(pk=pk)
        return make_response(request, sector)
