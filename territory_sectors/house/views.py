from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import HouseForm
from .models import House
from django.utils.translation import gettext_lazy as _


class HouseCreateView( SuccessMessageMixin, CreateView):
    form_class = HouseForm
    template_name = "house/create.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Create house'),
        'button_title': _('Create'),
    }
    success_message = _('House created successfully')



class HouseUpdateView(SuccessMessageMixin, UpdateView):
    model = House
    form_class = HouseForm
    template_name = "house/create.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Update house'),
        'button_title': _('Update'),
    }
    success_message = _('House updated successfully')

    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['houses'] = {
    #         self.object.id: House.objects.get(id=self.object.id)
    #     }
    #     return context
    #

class HouseListView(ListView):
    model = House
    template_name = "house/list.html"
    extra_context = {
        'remove_title': _('remove'),
        # 'houses': House.objects.all().in_bulk()
    }

class HouseDeleteView(SuccessMessageMixin,DeleteView):
    model = House
    template_name = "house/delete.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Remove house'),
        'button_title': _('Remove '),
        'message': _('Are you sure delete house '),
    }
    success_message = _('House deleted successfully')
