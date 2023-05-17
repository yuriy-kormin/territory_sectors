import django_filters
from django.utils.translation import gettext_lazy as _
from territory_sectors.house.models import House


class AddressFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(
        lookup_expr='icontains',
        label=_("Filter by address")
    )

    class Meta:
        model = House
        fields = ['address', ]
