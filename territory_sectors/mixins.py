from django.db.models import Count

from territory_sectors.house.models import House
from django.views.generic.list import MultipleObjectMixin


class HousesAddMixin(MultipleObjectMixin):

    def get_context_data(self, **kwargs):
        query = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['houses'] = House.objects.filter(
            flat__in=query
        ).distinct().annotate(Count('flat'))

        return context
