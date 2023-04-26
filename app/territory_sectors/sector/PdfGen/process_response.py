import io

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from .process_images import print_image
from .utils import get_xy


def draw_quadrants_lines(pdf):
    pdf.setDash(2, 2)  # Set dotted line style
    pdf.line(0, A4[0] / 2, A4[1], A4[0] / 2)  # Horizontal line
    pdf.line(A4[1] / 2, 0, A4[1] / 2, A4[0])  # Vertical line


def print_header_houses(pdf, sector):
    pdf.setFont("Arial", 14)
    total_flats = 0
    for i, house in enumerate(sector.get_houses_into()):
        flats_data = ''
        if (flat_count := house.flat_count()) > 0:
            total_flats += flat_count
            flats_data = f' ({flat_count} адресов)'
        pdf.drawString(*get_xy(2, 2.5 + (1 * i)), house.address + flats_data)
    # print header
    pdf.setFont("Arial", 26)
    header = f"Участок {sector.name} "
    if total_flats:
        header += f'({total_flats} адресов)'
    pdf.drawString(*get_xy(1, 1.5), header)


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
    pdf.save()
    buffer.seek(0)
    pdf = buffer.getvalue()
    buffer.close()
    # write the PDF content to the response object
    response.write(pdf)
    return response
