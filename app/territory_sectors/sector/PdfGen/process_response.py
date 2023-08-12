import io

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, portrait

from .generate_table import print_tables
from .process_images import print_image
from .utils import get_xy
from ..models import Sector


def draw_quadrants_lines(pdf):
    pdf.setDash(2, 2)  # Set dotted line style
    pdf.line(0, A4[0] / 2, A4[1], A4[0] / 2)  # Horizontal line
    pdf.line(A4[1] / 2, 0, A4[1] / 2, A4[0])  # Vertical line


def print_header_houses(pdf, sector):
    pdf.setFont("Arial", 14)
    total_flats = 0
    house_count = 0
    for i, house in enumerate(sector.get_houses_into()):
        flats_data = ''
        house_count += 1
        if (flat_count := house.flat_count()) > 0:
            total_flats += flat_count
            flats_data = f' ({flat_count} адресов)'
        pdf.drawString(*get_xy(2, 3 + (1 * i)), house.address + flats_data)
    # print header
    pdf.setFont("Arial", 26)
    header = f"Участок {sector.name}"
    pdf.drawString(*get_xy(1, 1.5), header)
    if total_flats and house_count > 1:
        pdf.setFont("Arial", 12)
        pdf.drawString(*get_xy(1, 2.2), f'({total_flats} адресов)')


def make_response(request, sector_instance):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=' \
                                      f'"{sector_instance.name}.pdf"'
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setPageSize(landscape(A4))
    draw_quadrants_lines(pdf)
    print_header_houses(pdf, sector_instance)
    for obj in 'map', 'qr':
        print_image(pdf, obj, request, sector_instance)
    pdf.showPage()

    pdf.setPageSize(portrait(A4))
    print_tables(pdf, sector_instance)
    pdf.showPage()

    pdf.save()
    buffer.seek(0)
    pdf = buffer.getvalue()
    buffer.close()
    # write the PDF content to the response object
    response.write(pdf)
    return response


from django.test import Client
from django.conf import settings

def process_backup_sectors():
    # client = Client()
    BACKUP_FOLDER = ""

    queryset = Sector.objects.all()[:1]

    for sector in queryset:
        # request = client.get('/')
        # pdf_response = make_response(request, sector)
        print( f'{settings.BASE_DIR=}')
