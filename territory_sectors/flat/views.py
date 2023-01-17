from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Flat
from territory_sectors.house.models import House
from django.utils.translation import gettext_lazy as _
from territory_sectors.mixins import HousesAddMixin

class FlatCreateView(CreateView):
    model = Flat
    fields = ['house', 'number', 'floor', 'way_desc']
    template_name = "flat/create.html"
    success_url = reverse_lazy('flat_list')
    extra_context = {
        'header': _('Create flat'),
        'button_title': _('Create'),
    }


class FlatListView(ListView, HousesAddMixin):
    model = Flat
    template_name = "flat/list.html"
    houses = Flat.objects.all()


class FlatDetailView(DetailView):
    model = Flat
    template_name = "flat/detail.html"
    # extra_context =
# class MarkUpdateView(LoginRequiredCustomMixin, SuccessMessageMixin,
#                      UpdateView):
#     model = Mark
#     form_class = MarkForm
#     template_name = "marks/create.html"
#     success_url = reverse_lazy('mark_list')
#     extra_context = {
#         'header': _('Update mark'),
#         'button_title': _('Update'),
#     }
#     success_message = _('Mark updated successfully')
#     permission_denied_message = _('Please login')
#
#
# class MarkDeleteView(LoginRequiredCustomMixin, DeleteProtectErrorMixin,
#                      DeleteView):
#     model = Mark
#     template_name = "marks/delete.html"
#     success_url = reverse_lazy('mark_list')
#     extra_context = {
#         'header': _('Remove mark'),
#         'button_title': _('Yes, remove'),
#         'message': _('Are you sure delete'),
#     }
#     raise_exception = False
#     permission_denied_message = _('Please login')
#     protected_error_message = _('Mark can\'t be deleted - on use now')
#     success_message = _('Mark was deleted successfully')
