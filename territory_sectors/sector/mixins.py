from django.contrib.gis.db.models.functions import AsGeoJSON
from django.db.models import Count
from django.views.generic.list import MultipleObjectMixin

from territory_sectors.house.models import House


class GeoJSONAnnotateMixin:
    def get_queryset(self):
        qs = super(GeoJSONAnnotateMixin, self).get_queryset()
        return qs.annotate(geojson=AsGeoJSON('contour'))


class AnnotateHouseFlatsCountsMixin:
    def get_queryset(self):
        qs = super(AnnotateHouseFlatsCountsMixin, self).get_queryset()
        return qs.annotate(
            flat_count=Count('house__flat')
        )


class ContextAddHousesMixin(MultipleObjectMixin):
    def get_context_data(self, **kwargs):
        """Add context."""
        context = super().get_context_data(**kwargs)
        context['houses'] = House.objects.all() \
            .annotate(Count('flat'))
        return context
