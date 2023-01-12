from django.db import models
from territory_sectors.house.models import House
from territory_sectors.language.models import Language


# Create your models here.
class Flat(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    house = models.ForeignKey(to=House, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()
    floor = models.IntegerField()
    way_desc = models.CharField(max_length=500)
    language = models.ForeignKey(to=Language, on_delete=models.SET_DEFAULT, default=1)
