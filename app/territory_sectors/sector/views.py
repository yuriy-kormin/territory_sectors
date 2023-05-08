from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SectorForm
from .models import Sector
from django.utils.translation import gettext_lazy as _
from .mixins import GeoJSONAnnotateMixin, ContextAllHousesIntoMixin, \
    CentroidAnnotateMixin
from ..mixins import LoginRequiredMixinCustom
from django.views import View


class SectorCreateView(LoginRequiredMixinCustom, ContextAllHousesIntoMixin,
                       SuccessMessageMixin, CreateView):
    model = Sector
    form_class = SectorForm
    template_name = "sector/create.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Create sector'),
        'button_title': _('Create'),
        'sectors': model.objects.all().annotate(
            geojson=AsGeoJSON('contour'),
        )
    }
    success_message = _('Sector created successfully')

    def form_valid(self, form):
        sector = form.save(commit=False)
        sector.assign_uuid()
        return super().form_valid(form)


class SectorUpdateView(LoginRequiredMixinCustom, CentroidAnnotateMixin,
                       ContextAllHousesIntoMixin, GeoJSONAnnotateMixin,
                       SuccessMessageMixin, UpdateView):
    model = Sector
    form_class = SectorForm
    template_name = "sector/create.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Update Sector'),
        'button_title': _('Update'),
        'sectors': model.objects.all().annotate(
            geojson=AsGeoJSON('contour')
        )
    }
    success_message = _('Sector updated successfully')

    # def get_context_data(self, **kwargs):
    #     """Add context."""
    #     context = super().get_context_data(**kwargs)
    #     url = self.request.build_absolute_uri(
    #         self.object.get_absolute_url(
    #             reverse("uuid", kwargs={'pk': self.object.uuid_id})
    #         )
    #     )
    #     img = make(url)
    #
    #     buffer = BytesIO()
    #     img.save(buffer)
    #     buffer.seek(0)
    #
    #     file_size = len(buffer.getvalue())
    #     file_name = f"qr_{self.id}.png"
    #     file_content = ContentFile(buffer.read(), name=file_name)
    #     img_data = base64.b64encode(
    #         InMemoryUploadedFile(
    #             file_content, None, file_name, 'image/png', file_size, None
    #         ).read()
    #     ).decode('utf-8')
    #
    #     context['qr_img_data'] = img_data
    #     return context


class SectorPrintView(LoginRequiredMixinCustom,
                      CentroidAnnotateMixin, UpdateView):
    model = Sector
    fields = ['name', 'uuid']
    template_name = "sector/print_sector_quadra.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'print_header': _('Sector '),
        'additional_rows': "*" * 2,
    }

    def get_context_data(self, **kwargs):
        """Add context."""
        context = super().get_context_data(**kwargs)
        context['url'] = self.request.build_absolute_uri(
            reverse_lazy(
                "uuid", kwargs={'pk': self.object.uuid_id})
        )
        if self.object.for_search:
            context['additional_rows'] = "*"*40
        return context


class SectorListView(LoginRequiredMixinCustom, ContextAllHousesIntoMixin,
                     GeoJSONAnnotateMixin, CentroidAnnotateMixin, ListView):
    model = Sector
    template_name = "sector/list.html"
    extra_context = {
        'remove_title': _('remove'),
    }

    def get_queryset(self):
        qs = super().get_queryset()

        status = self.extra_context.get('status', False)
        if status == 'for-serve':
            return qs.filter(for_search=False)
        elif status == 'for-search':
            return qs.filter(for_search=True)

        return qs


class SectorStatusHistory(LoginRequiredMixinCustom, ListView):
    model = Sector
    template_name = 'sector/history_status.html'
    extra_context = {
        'header': _('History statuses of '),
    }

    def get_queryset(self):
        sector_id = self.kwargs['pk']
        sector = Sector.objects.get(id=sector_id)
        history = sector.history.filter(history_type='~').order_by(
            '-history_date')
        return history

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['sector_name'] = self.model.objects.get(pk=pk).name
        return context


class SectorDeleteView(LoginRequiredMixinCustom, GeoJSONAnnotateMixin,
                       CentroidAnnotateMixin, SuccessMessageMixin, DeleteView):
    model = Sector
    template_name = "sector/delete.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Remove sector'),
        'button_title': _('Remove '),
        'message': _('Are you sure delete sector '),
    }
    success_message = _('Sector deleted successfully')


class SectorCheckInOutView(LoginRequiredMixinCustom, View):
    def post(self, request, *args, **kwargs):
        sector_id = self.kwargs.get('pk')
        data = request.body.decode()
        # sector = Sector.objects.get(id=sector_id)
        # sector.status
        # sector.save()

        # Return a JSON response with a success message
        return JsonResponse(
            {'message': f'Marker {sector_id} updated successfully.\n {data=}'})
    # model = Sector
    # form_class = SectorForm
    # template_name = "sector/checkinout.html"
    # success_url = reverse_lazy('sector_list')
    # extra_context = {
    #     'sectors': model.objects.all().annotate(
    #         geojson=AsGeoJSON('contour')
    #     )
    # }
    # success_message = _('Sector updated successfully')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # raise IOError(self.object.status.name)
    #     if self.object.status.name == 'assigned':
    #         context['header'] = _('Check out sector'),
    #         context['button_title'] = _('Check out'),
    #     if self.object.status.name in ('free', 'completed'):
    #         context['header'] = _('Check in sector'),
    #         context['button_title'] = _('Check in'),
    #     if self.object.status.name == 'under_construction':
    #         context['header'] = _(
    #         '<p style="color:red">Sector in service mode.Pay attention</p>'),
    #     return context
    #
    # def get_success_message(self, cleaned_data):
    #     return cleaned_data
    #     # if self.object.status.name == 'assigned':
    #     #     return _("Sector successfully checked out")
    #     # elif self.object.status.name in ('free', 'completed'):
    #     #     return _("Sector successfully checked in to ")
