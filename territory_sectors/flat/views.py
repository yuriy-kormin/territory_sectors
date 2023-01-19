from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FlatForm
from .mixins import HousesAddMixin
from .models import Flat
from django.utils.translation import gettext_lazy as _



class FlatCreateView(SuccessMessageMixin,CreateView):
    form_class = FlatForm
    template_name = "flat/create.html"
    success_url = reverse_lazy('flat_list')
    extra_context = {
        'header': _('Create flat'),
        'button_title': _('Create'),
    }
    success_message = _('Flat created successfully')


class FlatListView(HousesAddMixin, ListView):
    model = Flat
    template_name = "flat/list.html"
    extra_context = {
        "remove_title": _("remove")
    }


class FlatUpdateView(SuccessMessageMixin, UpdateView):
    model = Flat
    form_class = FlatForm
    template_name = "flat/create.html"
    success_url = reverse_lazy('flat_list')
    extra_context = {
        'header': _('Update Flat'),
        'button_title': _('Update'),
    }
    success_message = _('Flat updated successfully')


class FlatDeleteView(SuccessMessageMixin, DeleteView):
    model = Flat
    template_name = "flat/delete.html"
    success_url = reverse_lazy('flat_list')
    extra_context = {
        'header': _('Remove flat'),
        'button_title': _('Remove '),
        'message': _('Are you sure delete flat '),
    }
    success_message = _('Flat deleted successfully')
