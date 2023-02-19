from django.db import models

from territory_sectors.house.models import House
from territory_sectors.uuid_qr.models import Uuid
from django.contrib.gis.db import models as gis_models
from simple_history.models import HistoricalRecords


class SectorManager(models.Manager):
    def json_polygons(self):
        result = {}
        for sector in super(SectorManager, self).get_queryset():
            result[sector.id] = {
                'name': sector.name,
                'geojson': sector.contour.geojson,
            }
        return result


class Sector(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, null=True, unique=True)
    uuid = models.OneToOneField(to=Uuid, null=True, blank=True,
                                on_delete=models.SET_NULL)
    contour = gis_models.PolygonField(null=False, blank=False, srid=4326)
    objects = models.Manager()
    js = SectorManager.json_polygons
    history = HistoricalRecords()

    # flat_count = SectorManager.get_houses_into().aggregate(Sum('flat'))

    def __str__(self):
        return self.name

    def get_houses_into(self):
        return House.objects.filter(gps_point__intersects=self.contour)

    @classmethod
    def get_all_houses(cls):
        return House.objects.all()
# class Intersection(models.Model):
#     house = models.ForeignKey('House', on_delete=models.CASCADE)
#     sector = models.ForeignKey('Sector', on_delete=models.CASCADE)
