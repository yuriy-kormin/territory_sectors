from django.db import models
from django.contrib.gis.db import models as gis_models
from territory_sectors.sector.models import Sector


# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    floor_amount = models.IntegerField(null=True)
    entrances = models.IntegerField(null=True)
    sector = models.ForeignKey(to=Sector, on_delete=models.SET_NULL,
                               null=True, blank=True)

    gps_point = gis_models.PointField(null=False, blank=False, srid=4326)
    def __str__(self):
        return self.address

    # def get_gps(self):
    #     return self.gps_point.x
