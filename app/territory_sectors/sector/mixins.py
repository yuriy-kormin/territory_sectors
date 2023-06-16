from django.contrib.gis.db.models.functions import AsGeoJSON, Centroid
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from .models import Sector
from natsort import natsorted


class NatSortMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        return natsorted(queryset,
                         key=lambda s: (s.status_id, s.name)
                         )


class GeoJSONAnnotateMixin:
    def get_queryset(self):
        qs = super(GeoJSONAnnotateMixin, self).get_queryset()
        return qs.annotate(geojson=AsGeoJSON('contour'))


class CentroidAnnotateMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(centroid=Centroid('contour'))


class ContextAllHousesIntoMixin:
    def get_context_data(self, **kwargs):
        """Add list all houses into context"""
        context = super().get_context_data(**kwargs)
        houses = Sector.get_all_houses() \
            .annotate(flat_count=Count('flat'))
        if status := context.get('status'):
            if status == 'for-serve':
                houses = houses.filter(for_search=False)
            elif status == 'for-search':
                houses = houses.filter(for_search=True)
        context['houses'] = houses
        return context


class AddContextGetChangesHistoryMixin:

    def get_queryset(self):

        def get_related_status(obj):
            try:
                name = obj.status.name
            except (ObjectDoesNotExist, AttributeError):
                return
            return name

        qs = super().get_queryset()

        for item in qs:
            groups = []
            history = item.get_changes_history().reverse()
            if slice_indexes := [i+1 for i, v in enumerate(history)
                                 if get_related_status(v) == 'completed']:
                start = 0
                for index in slice_indexes:
                    groups.append(history[start:index])
                    start = index
                groups.append(history[index:])
            else:
                groups = [history]
            item.assignments = groups

        return qs
