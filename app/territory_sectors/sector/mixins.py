from django.contrib.gis.db.models.functions import AsGeoJSON, Centroid
from django.core.exceptions import ObjectDoesNotExist
import json
from django.db.models import Count
from .models import Sector
from natsort import natsorted
from itertools import groupby

from ..consts_from_js import search_status


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
                    "id": f'{house.id}',
                    "color": search_status[house.for_search]
                },
                #     "popup": render_to_string(
                #         'sector/house_popup.html',
                #         {'house': house})
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

            item.assignments = groups[-3:]

        return qs


class AddContextFullJSONMixin(GeoJSONAnnotateMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = super().get_queryset()
        sectors = []
        for sector in qs:
            sector_data = sector.get_js_source()
            sectors.append(sector_data)

        context['sectors_json'] = json.dumps(sectors)
        return context


class AddDebtorsMixin:
    def get_context_data(self, **kwargs):
        """Add list of debtors into context"""

        DEBT_AGE = 4
        DEBT_PRE_AGE = 3

        def get_related_info(sector):
            return {
                'name': sector.name,
                'id': sector.id,
                'status': sector.status.name,
                'status_age': sector.get_status_age_in_months(),
                'houses': {house.id: house.address
                           for house in sector.get_houses_into()}
            }

        context = super().get_context_data(**kwargs)
        sectors = Sector.objects.filter(status__name__contains='assigned'). \
            select_related('status').order_by('assigned_to')

        debtors = [
            s for s in sectors if s.get_status_age_in_months() >= DEBT_AGE]
        pre_debtors = [s for s in sectors if
                       DEBT_PRE_AGE <= s.get_status_age_in_months() < DEBT_AGE
                       ]

        context['debtors'] = {
            debtor: list(map(get_related_info, sectors))
            for debtor, sectors in groupby(
                debtors,
                key=lambda sector: str(sector.assigned_to).strip().lower()
            )
        }
        context['pre_debtors'] = {
            debtor: list(map(get_related_info, sectors))
            for debtor, sectors in groupby(
                pre_debtors,
                key=lambda sector: str(sector.assigned_to).strip().lower()
            )
        }

        return context
