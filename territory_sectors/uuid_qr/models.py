from django.db import models
from shortuuid.django_fields import ShortUUIDField
from territory_sectors.sector.models import Sector
from territory_sectors.house.models import House
from territory_sectors.flat.models import Flat
class Uuid(models.Model):
    id = ShortUUIDField(primary_key=True,
                        length=10,
                        max_length=10,
                        auto_created=True,)
    sector = models.ForeignKey(to=Sector, null=True, on_delete=models.SET_NULL)
    house = models.ForeignKey(to=House, null=True, on_delete=models.SET_NULL)
    flat = models.ForeignKey(to=Flat, null=True, on_delete=models.SET_NULL)
