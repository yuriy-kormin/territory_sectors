import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from django.conf import settings
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def get_xy(x_cm, y_cm):
    # library calculate coordinates from bottom left corner.
    # function convert value to human-readable from top-left
    # its for landscape page only

    return x_cm * cm, A4[0] - y_cm * cm


def set_font():
    font_path = os.path.join(
        settings.BASE_DIR,
        'territory_sectors',
        'sector',
        'PdfGen',
        'font',
        'arial.ttf'
    )
    pdfmetrics.registerFont(TTFont('Arial', font_path))
