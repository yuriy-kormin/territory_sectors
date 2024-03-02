from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Status(models.Model):
    name_options = (
        ('free', _('free')),
        ('assigned', _('assigned')),
        ("under_construction", _('under_construction')),
        ("completed", _('completed')),
        ("for_event", _('for_event')),
        ("for_event_done", _('for_event_done')),
    )
    name = models.CharField(max_length=200, unique=True,
                            choices=name_options,
                            default='free')
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    # pass
