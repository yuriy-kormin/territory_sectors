from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import HouseForm
from .mixins import CountFlatsMixin
from .models import House
from django.utils.translation import gettext_lazy as _


class HouseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = HouseForm
    template_name = "house/create.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Create house'),
        'button_title': _('Create'),
        'langs': House.get_lang_list_qs(),
    }
    success_message = _('House created successfully')


class HouseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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

    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    #     return response

    # def form_valid(self, form):
    #     flat_count = self.request.POST.get('flats_data')
    #     super().form_valid(form)
    #     raise IOError(self.request.POST)
    #     #
    #     house = House.objects.get(
    #         address=self.request.POST
    #     )
    #
    #     if flat_count:
    #         flats = []
    #         for i in range(1, flat_count + 1):
    #             flats.append(
    #                 Flat(
    #                     house=house,
    #                     number=self.request.POST.get(f'number_{i}'),
    #                     entrance=self.request.POST.get(f'entrance_{i}'),
    #                     floor=self.request.POST.get(f'floor_{i}'),
    #                     way_desc=self.request.POST.get(f'desc_{i}'),
    #                 )
    #             )
    #         Flat.objects.bulk_create(flats)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['houses'] = {
    #         self.object.id: House.objects.get(id=self.object.id)
    #     }
    #     return context
    #


class HouseListView(LoginRequiredMixin, CountFlatsMixin, ListView):
    model = House
    template_name = "house/list.html"
    # queryset = House.objects.order_by('address')
    extra_context = {
        'remove_title': _('remove'),
    }
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        context['page_obj'] = page_obj
        return context


class HouseDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = House
    template_name = "house/delete.html"
    success_url = reverse_lazy('house_list')
    extra_context = {
        'header': _('Remove house'),
        'button_title': _('Remove '),
        'message': _('Are you sure delete house '),
    }
    success_message = _('House deleted successfully')
