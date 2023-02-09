from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SectorForm
from .models import Sector
from django.utils.translation import gettext_lazy as _
from .mixins import GeoJSONAnnotateMixin, ContextAddHousesMixin
from ..house.models import House


# from territory_sectors.house.models import House


class SectorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = SectorForm
    template_name = "sector/create.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Create sector'),
        'button_title': _('Create'),
    }
    success_message = _('Sector created successfully')


class SectorUpdateView(LoginRequiredMixin, GeoJSONAnnotateMixin,
                       SuccessMessageMixin, UpdateView):
    model = Sector
    form_class = SectorForm
    template_name = "sector/create.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Update Sector'),
        'button_title': _('Update'),
    }
    success_message = _('Sector updated successfully')


#     #
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['houses'] = {
#     #         self.object.id: House.objects.get(id=self.object.id)
#     #     }
#     #     return context
#     #

class SectorListView(LoginRequiredMixin, GeoJSONAnnotateMixin,
                     ListView, ContextAddHousesMixin):
    model = Sector
    template_name = "sector/list.html"
    extra_context = {
        'remove_title': _('remove'),
    }


class SectorDeleteView(LoginRequiredMixin, GeoJSONAnnotateMixin,
                       SuccessMessageMixin, DeleteView):
    model = Sector
    template_name = "sector/delete.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Remove sector'),
        'button_title': _('Remove '),
        'message': _('Are you sure delete sector '),
    }
    success_message = _('Sector deleted successfully')
