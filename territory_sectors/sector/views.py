from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SectorForm
from .models import Sector
from django.utils.translation import gettext_lazy as _
from .mixins import GeoJSONAnnotateMixin, ContextAddHousesMixin, \
    CentoidAnnotateMixin


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
    form_class = SectorForm
    template_name = "sector/create.html"
    success_url = reverse_lazy('sector_list')
    extra_context = {
        'header': _('Create sector'),
        'button_title': _('Create'),
    }
    success_message = _('Sector created successfully')




class SectorUpdateView(LoginRequiredMixin,CentoidAnnotateMixin,
                       ContextAddHousesMixin, GeoJSONAnnotateMixin,
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
                     GeoJSONAnnotateMixin,CentoidAnnotateMixin,
                     ListView):
    model = Sector
    # paginate_by = model
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
