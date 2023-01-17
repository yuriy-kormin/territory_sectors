from territory_sectors.house.models import House
from django.views.generic.list import MultipleObjectMixin

class HousesAddMixin(MultipleObjectMixin):
    houses = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['houses'] = House.objects.filter(
            flat__in=self.houses
        ).distinct().in_bulk()

        return context
