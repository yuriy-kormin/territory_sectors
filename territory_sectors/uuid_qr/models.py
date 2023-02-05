from django.db import models
from shortuuid.django_fields import ShortUUIDField
# from territory_sectors.sector.models import Sector
# from territory_sectors.house.models import House
# from territory_sectors.flat.models import Flat
# import qrcode
# from io import BytesIO
# from django.core.files import File
# from PIL import Image, ImageDraw


class Uuid(models.Model):
    id = ShortUUIDField(primary_key=True,
                        length=10,
                        max_length=10,
                        auto_created=True, )

    # qr_image = models.ImageField(blank=True, null=True, upload_to='QRCode')

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

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
