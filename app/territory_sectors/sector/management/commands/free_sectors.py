from django.core.management.base import BaseCommand
from territory_sectors.sector.models import Sector
from territory_sectors.status.models import Status


class Command(BaseCommand):
    help = 'Filters books by status and prints them'

    def handle(self, *args, **kwargs):
        # update completed status to free if get_status_age_in_months
        # more AUTO_FREE_MONTH
        free_status = Status.objects.filter(name='free').first()

        for s in Sector.objects.filter(status__name='completed'):
            age = s.get_status_age_in_months()
            if age >= Sector.AUTO_FREE_MONTH:
                s.status = free_status
                s.save()
                print(f"{s.name} was free after {age} months completed")
