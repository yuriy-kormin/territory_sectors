from django.db import models
from django.contrib.gis.db import models as gis_models
from territory_sectors.uuid_qr.models import Uuid
from simple_history.models import HistoricalRecords
from territory_sectors.language.models import Language
import json
from django.core.serializers.json import DjangoJSONEncoder


class HouseManager(models.Manager):
    def flats_json(self):
        flats = self.flat_set.values(
            'id', 'entrance', 'floor', 'number', 'way_desc',
            'language'
        )
        return json.dumps(list(flats), cls=DjangoJSONEncoder)


class House(models.Model):
    MAX_IMAGE_RESOLUTION = 1024
    PREVIEW_IMAGE_RESOLUTION = 100

    address = models.CharField(max_length=300, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    floor_amount = models.IntegerField(null=True)
    entrances = models.IntegerField(null=True)
    image = models.ImageField(upload_to='house/', null=True, blank=True)
    image_preview = models.ImageField(upload_to='house/', null=True, blank=True)
    # sector = models.ForeignKey('Sector', on_delete=models.CASCADE,
    #                            related_name='sectors')

    # lift = ???
    # sector = models.ForeignKey(to=Sector, on_delete=models.SET_NULL,
    #                            null=True, blank=True)
    for_search = models.BooleanField(default=True, null=False, blank=False)
    desc = models.CharField(max_length=1500, default='', null=True, blank=True)
    gps_point = gis_models.PointField(null=False, blank=False, srid=4326)
    uuid = models.OneToOneField(to=Uuid, null=True, blank=True,
                                on_delete=models.SET_NULL)
    history = HistoricalRecords()
    flats_json = HouseManager.flats_json
    # flats_ids = HouseManager
    # Shop.objects.annotate(
    #     contained_points=
    #     Location.objects.values('area').filter(
    #         area__intersects=OuterRef('location')
    #     )[:1],
    # ).values()
    # House.objects.annotate(contain_sec = Sector.objects.values('contour')
    # .filter(contour__intersects=OuterRef('gps_point'))[:1]).values('contain_sec')
    # - работает - но только в сторону annotate with sector instance

    # class Meta:
    #     ordering = ['house', 'entrance]
    #
    def __str__(self):
        return self.address

    def gps_pos(self):
        return f'{self.gps_point.x}, {self.gps_point.y}'

    def get_ru_flats(self):
        return self.flat_set.filter(language_id=1)

    # def get_sectors(self):
    #     return Sector.objects.filter(contour__intersects=self.gps_point)
    # def flats_join_ids(self):
    #     flats = self.flat_set.values_list('id', flat=True)
    #     return ",".join(map(lambda x: str(x), flats))

    # def flats_json(self):
    #     flats = self.flat_set.values(
    #         'id', 'entrance', 'floor', 'number', 'way_desc',
    #         'language__id', 'language__name'
    #     )
    #     return json.dumps(list(flats), cls=DjangoJSONEncoder)
    def flat_count(self):
        return self.flat_set.count()

    @classmethod
    def get_lang_list_qs(cls):
        return Language.objects.all()
