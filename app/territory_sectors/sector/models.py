import json

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from urllib.parse import quote

from django.db.models import F, Value
from django.db.models.functions import Concat
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
    history = HistoricalRecords(related_name='historical')
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
        return House.objects.prefetch_related('flat_set')

    def get_changes_history(self):
        def get_related_status(obj):
            try:
                name = obj.status.name
            except (ObjectDoesNotExist, AttributeError):
                return
            return name

        history = self.history.prefetch_related('status',
                                                'history_user').annotate(
            full_name=Concat(
                F('history_user__last_name'),
                Value(' '),
                F('history_user__first_name')
            )
        ).order_by('history_date')
        exclude_records = []
        if not get_related_status(history[0]):
            exclude_records.append(history[0].history_id)
        prev_record = history[0]
        if len(history) > 1:
            for record in history[1:]:
                if len(set(
                        map(get_related_status, (record, prev_record))
                )) == 1 and record.assigned_to == prev_record.assigned_to:
                    exclude_records.append(record.history_id)
                else:
                    prev_record = record
        return history.exclude(history_id__in=exclude_records).reverse()

    def get_js_source(self):
        return {
            'id': self.id,
            'type': 'Feature',
            'properties': {
                'name': self.status.name if self.status else None,
                'for_search': self.for_search,
                'status': self.status.name if self.status else None,
                'id': self.id,
            },
            'geometry': json.loads(self.geojson)
            # to fetch this qs must be annotated with
            # geojson=AsGeoJSON('contour'))
        }
