from django.contrib.gis.db.models.functions import AsGeoJSON
from django.db.models import Count


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
