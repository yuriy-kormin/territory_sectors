from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm


def get_xy(x_cm, y_cm):
    # library calculate coordinates from bottom left corner.
    # function convert value to human-readable from top-left
    # its for landscape page only

    return x_cm * cm, A4[0] - y_cm * cm

#
# import os
# from datetime import datetime
# from django.core.wsgi import get_wsgi_application
# from django.test.client import RequestFactory
# from your_django_app.models import YourModel  # Replace with your actual model import
# from your_django_app.lib import generate_pdf_backup  # Import your PDF generation function
#
# # Replace with the folder where you want to save the generated PDFs
# BACKUP_FOLDER = "/path/to/backup/folder/"
#
# def main():
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
#     application = get_wsgi_application()
#     request_factory = RequestFactory()
#
#     queryset = YourModel.objects.all()
#
#     for instance in queryset:
#         request = request_factory.get('/')
#         pdf_response = generate_pdf_backup(request, instance)
#
#         if pdf_response and pdf_response.status_code == 200 and pdf_response['Content-Type'] == 'application/pdf':
#             now = datetime.now()
#             date_folder = now.strftime("%Y-%m-%d")
#             backup_folder = os.path.join(BACKUP_FOLDER, date_folder)
#
#             if not os.path.exists(backup_folder):
#                 os.makedirs(backup_folder)
#
#             pdf_filename = f"{instance.id}.pdf"
#             pdf_path = os.path.join(backup_folder, pdf_filename)
#
#             with open(pdf_path, 'wb') as pdf_file:
#                 pdf_file.write(pdf_response.content)
#
#             print(f"Generated and saved PDF backup for instance {instance.id}.")
#
# if __name__ == "__main__":
#     main()
