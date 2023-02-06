from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=200, unique=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
