from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from .filters import AddressFilter
from .forms import HouseForm
from .mixins import CountFlatsMixin, ImageResizeBeforeMixin
from .models import House
from django.utils.translation import gettext_lazy as _
from ..mixins import LoginRequiredMixinCustom


class HouseCreateView(LoginRequiredMixinCustom, ImageResizeBeforeMixin,
                      SuccessMessageMixin, CreateView):
    form_class = HouseForm
    template_name = "house/create.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Create house'),
        'button_title': _('Create'),
        'langs': House.get_lang_list_qs(),
    }
    success_message = _('House created successfully')


class HouseUpdateView(LoginRequiredMixinCustom, ImageResizeBeforeMixin,
                      SuccessMessageMixin, UpdateView):
    model = House
    form_class = HouseForm
    template_name = "house/create.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Update house'),
        'button_title': _('Update'),
        'langs': House.get_lang_list_qs(),
    }
    success_message = _('House updated successfully')


class HouseListView(LoginRequiredMixinCustom, CountFlatsMixin, FilterView,
                    ListView):
    filterset_class = AddressFilter
    model = House
    template_name = "house/list.html"
    extra_context = {
        'remove_title': _('Remove'),
        'select': _('Select')
    }
    ordering = 'address'


class HouseDeleteView(LoginRequiredMixinCustom,
                      SuccessMessageMixin, DeleteView):
    model = House
    template_name = "house/delete.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Remove house'),
        'button_title': _('Remove '),
        'message': _('Are you sure delete house '),
    }
    success_message = _('House deleted successfully')
