import io

import requests
from PIL import Image
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, portrait
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from qr_code.qrcode.maker import make_qr_code_image
from .models import Sector
from qr_code.qrcode.utils import QRCodeOptions
from .PdfGen.process_response import make_response


pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

class SectorPrintPDF(View):
    def get(self, request, pk):

        sector = Sector.objects.get(pk=pk)
        return make_response(request, sector)
        #
        #
        # # Second page: Portrait with a table
        # pdf.setPageSize(portrait(A4))
        # styles = getSampleStyleSheet()
        # data = [['Name', 'Age', 'Gender'],
        #         ['John', '30', 'Male'],
        #         ['Jane', '25', 'Female'],
        #         ['Bob', '42', 'Male'],
        #         ['Alice', '38', 'Female']]
        # table = Table(data)
        # table.setStyle(TableStyle([
        #     ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        #     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        #     ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        #     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        #     ('FONTSIZE', (0, 0), (-1, 0), 14),
        #     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        #     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        #     ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        #     ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        #     ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        #     ('FONTSIZE', (0, 1), (-1, -1), 12),
        #     ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        #     ('BACKGROUND', (0, -1), (-1, -1), colors.grey),
        #     ('TEXTCOLOR', (0, -1), (-1, -1), colors.whitesmoke),
        #     ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
        #     ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        #     ('FONTSIZE', (0, -1), (-1, -1), 14),
        #     ('TOPPADDING', (0, -1), (-1, -1), 12),
        # ]))
        # table.wrapOn(pdf, A4[0] - 2 * cm, A4[1] - 6 * cm)
        # table.drawOn(pdf, 1 * cm, 16 * cm)
        # pdf.showPage()

