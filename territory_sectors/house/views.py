from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import House
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import Point
from territory_sectors.mixins import HousesAddMixin


class HouseCreateView(CreateView):
    model = House
    fields = [
        'address',
        'floor_amount',
        'entrances',
        'sector',
        'uuid',
    ]
    template_name = "house/create.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Create house'),
        'button_title': _('Create'),
        # 'markers': {0: Point(41.6115, 41.632645)}
    }

class HouseListView(ListView):
    model = House
    template_name = "house/list.html"
    extra_context = {
        'houses': House.objects.all().in_bulk()
    }


class HouseDetailView(DetailView):
    model = House
    template_name = "house/detail.html"