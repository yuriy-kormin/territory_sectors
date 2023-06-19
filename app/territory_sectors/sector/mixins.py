import re

from django.contrib.gis.db.models.functions import AsGeoJSON, Centroid
from django.core.exceptions import ObjectDoesNotExist
import json
from django.db.models import Count
from django.template.loader import render_to_string

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
            .annotate(flat_count=Count('flat'),
                      geojson=AsGeoJSON('gps_point')
                      )
        if status := context.get('status'):
            if status == 'for-serve':
                houses = houses.filter(for_search=False)
            elif status == 'for-search':
                houses = houses.filter(for_search=True)
        context['houses'] = houses
        result_json = []
        for house in houses:
            result_json.append({
                "id": f'house_{house.id}',
                "type": "Feature",
                "geometry": json.loads(house.geojson),
                "properties": {
                    "name": f'{house.flat_count}',
                    "title": f'{house.flat_count}',
                    "mark": house.for_search if house.for_search
                    else 'default',
                    "id": f'house_{house.id}',
                },
                "popup": render_to_string(
                    'sector/house_popup.html',
                    {'house': house})
            })

        context['houses_json'] = json.dumps(result_json)
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
            if slice_indexes := [i + 1 for i, v in enumerate(history)
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


class AddContextFullJSONMixin(GeoJSONAnnotateMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = super().get_queryset()
        sectors = []
        for sector in qs:
            sector_data = sector.get_js_source()
            sector_data['popup'] = re.sub(
                r'\s{2}',
                '',
                render_to_string(
                    'sector/sector_popup.html',
                    {'sector': sector})
            )
            sectors.append(sector_data)

        context['sectors_json'] = json.dumps(sectors)
        return context
