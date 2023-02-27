from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SectorForm
from .models import Sector
from django.utils.translation import gettext_lazy as _
from .mixins import GeoJSONAnnotateMixin, ContextAddHousesMixin, \
    CentroidAnnotateMixin


# from territory_sectors.uuid_qr.mixins import ContextAddQrImgData
# import base64
# from io import BytesIO
# from qrcode import make
# # from django.core.files import File
# from django.core.files.base import ContentFile
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from django.urls import reverse


class SectorCreateView(LoginRequiredMixin,
                       ContextAddHousesMixin, SuccessMessageMixin, CreateView):
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


class SectorUpdateView(LoginRequiredMixin, CentroidAnnotateMixin,
                       ContextAddHousesMixin, GeoJSONAnnotateMixin,
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


class SectorListView(LoginRequiredMixin, ContextAddHousesMixin,
                     GeoJSONAnnotateMixin, CentroidAnnotateMixin,
                     ListView):
    model = Sector
    # paginate_by = model
    template_name = "sector/list.html"
    extra_context = {
        'remove_title': _('remove'),
    }


class SectorStatusHistory(LoginRequiredMixin, ListView):
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
