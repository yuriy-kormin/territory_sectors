from django.db import models
from territory_sectors.uuid_qr.models import Uuid


class Sector(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, null=True)
    uuid = models.OneToOneField(to=Uuid, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
