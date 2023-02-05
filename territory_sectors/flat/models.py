from django.db import models
from territory_sectors.house.models import House
from territory_sectors.language.models import Language
from territory_sectors.uuid_qr.models import Uuid
from simple_history.models import HistoricalRecords


# Create your models here.
class Flat(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    house = models.ForeignKey(to=House, on_delete=models.CASCADE)
    number = models.CharField(max_length=300, null=True, blank=True)
    entrance = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    way_desc = models.CharField(max_length=500)
    language = models.ForeignKey(to=Language, on_delete=models.SET_DEFAULT, default=1)
    uuid = models.OneToOneField(to=Uuid, null=True, blank=True, on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.house.address} - {self.entrance} - {self.floor} {self.number}'
