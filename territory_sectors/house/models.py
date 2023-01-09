from django.db import models
from territory_sectors.sector.models import Sector


# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    house = models.ForeignKey(to=Sector, on_delete=models.SET_NULL, null=True, blank=True)
