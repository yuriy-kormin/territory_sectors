import json

from django.db import models
from territory_sectors.uuid_qr.models import Uuid
from django.contrib.gis.db import models as gis_models


class SectorManager(models.Manager):
    def json_polygons(self):
        result = {}
        for sector in super().get_queryset():
            result[sector.id] ={
                'name': sector.name,
                'geojson': sector.contour.geojson,
            }
        return result


class Sector(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, null=True)
    uuid = models.OneToOneField(to=Uuid, null=True, blank=True, on_delete=models.SET_NULL)
    contour = gis_models.PolygonField(null=False, blank=False, srid=4326)
    objects = models.Manager()
    js = SectorManager()

    # var polygon = {{obj.geom.transform(4326).geojson}};
    def __str__(self):
        return self.name
