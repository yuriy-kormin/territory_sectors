import base64

from django.db import models
from shortuuid.django_fields import ShortUUIDField
# from territory_sectors.sector.models import Sector
# from territory_sectors.house.models import House
# from territory_sectors.flat.models import Flat
# import qrcode
from io import BytesIO
from qrcode import make
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse
# from django.core.files import File
# from PIL import Image, ImageDraw


class Uuid(models.Model):
    id = ShortUUIDField(primary_key=True,
                        length=10,
                        max_length=10,
                        auto_created=True,
                        )

    # qr_image = models.ImageField(blank=True, null=True, upload_to='QRCode')

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    # def get_qr_img(self):
    #     self.
    #     url =    reverse("uuid", kwargs={'pk': self.pk})
    #     img = make(url)
    #
    #     buffer = BytesIO()
    #     img.save(buffer)
    #     buffer.seek(0)
    #
    #     file_size = len(buffer.getvalue())
    #     file_name = f"qr_{self.id}.png"
    #     file_content = ContentFile(buffer.read(), name=file_name)
    #     return base64.b64encode(
    #         InMemoryUploadedFile(
    #             file_content, None, file_name, 'image/png', file_size, None
    #         ).read()
    #     ).decode('utf-8')
    # def save(self, *args, **kwargs):
    #     qr_image = qrcode.make(self.name)
    #     qr_offset = Image.new('RGB', (310, 310), 'white')
    #     draw_img = ImageDraw.Draw(qr_offset)
    #     qr_offset.paste(qr_image)
    #     file_name = f'{self.name}-{self.id}qr.png'
    #     stream = BytesIO()
    #     qr_offset.save(stream, 'PNG')
    #     self.qr_image.save(file_name, File(stream), save=False)
    #     qr_offset.close()
    #     super().save(*args, **kwargs)
