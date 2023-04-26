from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm


def get_xy(x_cm, y_cm):
    # library calculate coordinates from bottom left corner.
    # function convert value to human-readable from top-left
    # its for landscape page only

    return x_cm * cm, A4[0] - y_cm * cm
