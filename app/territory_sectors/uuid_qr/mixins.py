# import base64
# from io import BytesIO
# from qrcode import make
# # from django.core.files import File
# from django.core.files.base import ContentFile
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from django.urls import reverse
#
#
# class ContextAddQrImgData:
#     def get_context_data(self, **kwargs):
#         """Add context."""
#         context = super().get_context_data(**kwargs)
#         url = self.request.build_absolute_uri(
#             self.object.get_absolute_url(
#                 reverse("uuid", kwargs={'pk': self.pk})
#             )
#         )
#         img = make(url)
#
#         buffer = BytesIO()
#         img.save(buffer)
#         buffer.seek(0)
#
#         file_size = len(buffer.getvalue())
#         file_name = f"qr_{self.id}.png"
#         file_content = ContentFile(buffer.read(), name=file_name)
#         img_data = base64.b64encode(
#             InMemoryUploadedFile(
#                 file_content, None, file_name, 'image/png', file_size, None
#             ).read()
#         ).decode('utf-8')
#
#         context['qr_img_data'] = img_data
#         return context
