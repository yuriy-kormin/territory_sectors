from django.db import models
from shortuuid.django_fields import ShortUUIDField
# from territory_sectors.sector.models import Sector
# from territory_sectors.house.models import House
# from territory_sectors.flat.models import Flat
class Uuid(models.Model):
    id = ShortUUIDField(primary_key=True,
                        length=10,
                        max_length=10,
                        auto_created=True,)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
