from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SectorForm
from .models import Sector
from django.utils.translation import gettext_lazy as _
from .mixins import GeoJSONAnnotateMixin


class SectorCreateView(SuccessMessageMixin, CreateView):
    form_class = SectorForm
    template_name = "sector/create.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Create sector'),
        'button_title': _('Create'),
    }
    success_message = _('Sector created successfully')


class SectorUpdateView(SuccessMessageMixin, UpdateView):
    pass


#     model = House
#     form_class = HouseForm
#     template_name = "house/create.html"
#     success_url = reverse_lazy('house_list')
#     extra_context = {
#         'header': _('Update house'),
#         'button_title': _('Update'),
#     }
#     success_message = _('House updated successfully')
#
#     #
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['houses'] = {
#     #         self.object.id: House.objects.get(id=self.object.id)
#     #     }
#     #     return context
#     #

class SectorListView(GeoJSONAnnotateMixin, ListView):
    model = Sector
    template_name = "sector/list.html"
    extra_context = {
        'remove_title': _('remove'),
    }


class SectorDeleteView(GeoJSONAnnotateMixin,SuccessMessageMixin, DeleteView):
    model = Sector
    template_name = "sector/delete.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Remove sector'),
        'button_title': _('Remove '),
        'message': _('Are you sure delete sector '),
    }
    success_message = _('Sector deleted successfully')
