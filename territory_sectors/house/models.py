from django.db import models
from django.contrib.gis.db import models as gis_models
# from territory_sectors.sector.models import Sector
from territory_sectors.uuid_qr.models import Uuid
from simple_history.models import HistoricalRecords


# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=300, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    floor_amount = models.IntegerField(null=True)
    entrances = models.IntegerField(null=True)
    # lift = ???
    # sector = models.ForeignKey(to=Sector, on_delete=models.SET_NULL,
    #                            null=True, blank=True)

    gps_point = gis_models.PointField(null=False, blank=False, srid=4326)
    uuid = models.OneToOneField(to=Uuid, null=True, blank=True,
                                on_delete=models.SET_NULL)
    history = HistoricalRecords()

    # Shop.objects.annotate(
    #     contained_points=
    #     Location.objects.values('area').filter(
    #         area__intersects=OuterRef('location')
    #     )[:1],
    # ).values()
    # House.objects.annotate(contain_sec = Sector.objects.values('contour').filter(contour__intersects=OuterRef('gps_point'))[:1]).values('contain_sec')
    # - работает - но только в сторону annotate with sector instance

    def __str__(self):
        return self.address

    def gps_pos(self):
        return f'{self.gps_point.x}, {self.gps_point.y}'

