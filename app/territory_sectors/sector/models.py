import json

from django.db import models
from urllib.parse import quote
from territory_sectors.house.models import House
from territory_sectors.status.models import Status
from territory_sectors.uuid_qr.models import Uuid
from django.contrib.gis.db import models as gis_models
from simple_history.models import HistoricalRecords
from geojson import Feature, Point, FeatureCollection


class SectorManager(models.Manager):
    def json_polygons(self):
        result = {}
        for sector in super(SectorManager, self).get_queryset():
            result[sector.id] = {
                'name': sector.name,
                'geojson': sector.contour.geojson,
            }
        return result


class StatManager(models.Manager):
    def total_count(self):
        return self.count()

    def free_count(self):
        return self.filter(status__name='free').count()

    def assigned_count(self):
        return self.filter(status__name='assigned').count()

    def completed_count(self):
        return self.filter(status__name='completed').count()


class Sector(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, null=True, unique=True)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    for_search = models.BooleanField(default=False, null=False, blank=False)
    assigned_to = models.CharField(max_length=300, null=True, blank=True)
    uuid = models.OneToOneField(to=Uuid, null=True, blank=True,
                                on_delete=models.SET_NULL)
    contour = gis_models.PolygonField(null=False, blank=False, srid=4326)
    objects = models.Manager()
    js = SectorManager.json_polygons
    history = HistoricalRecords()
    stat = StatManager()

    def __str__(self):
        return self.name

    def get_houses_into(self):
        return House.objects.filter(
            gps_point__intersects=self.contour,
            for_search=self.for_search
        )

    def get_mapbox_json(self):
        houses = self.get_houses_into()
        features = []
        for house in houses:
            feature = Feature(
                geometry=Point(house.gps_point),
                properties={
                    "marker-color": "#B917FC",
                    "marker-size": "large",
                    "text": "some text",
                }
            )
            features.append(feature)
        feature_collection = FeatureCollection(features)
        geojson_str = json.dumps(feature_collection)
        return quote(geojson_str)

    def get_center_coords(self):
        return Point(self.contour.centroid)['coordinates']

    def assign_uuid(self):
        self.uuid = Uuid.objects.create()

    @classmethod
    def get_all_houses(cls):
        return House.objects.all()

# class Intersection(models.Model):
#     house = models.ForeignKey('House', on_delete=models.CASCADE)
#     sector = models.ForeignKey('Sector', on_delete=models.CASCADE)

# class SectorStatus(models.Model):
#     sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
#     status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
#     date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     issued_to_publisher = models.CharField(max_length=300, null=True)
