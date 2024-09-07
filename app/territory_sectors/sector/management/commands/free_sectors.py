from django.core.management.base import BaseCommand
from territory_sectors.sector.models import Sector
from territory_sectors.status.models import Status


class Command(BaseCommand):
    help = 'Filters books by status and prints them'  # Description of your command

    def handle(self, *args, **kwargs):
        # update completed status to free if get_status_age_in_months more AUTO_FREE_MONTH
        free_status = Status.objects.filter(name='free').first()

        for s in self.__class__.objects.filter(status__name='completed'):
            if s.get_status_age_in_months() >= self.AUTO_FREE_MONTH:
                s.status = free_status
                s.save()