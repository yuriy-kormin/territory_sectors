from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.db.models.functions import Centroid
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from territory_sectors.uuid_qr.models import Uuid

from .mixins import StatMixin
from .sector.mixins import AddContextGetChangesHistoryMixin
from .sector.models import Sector


class IndexView(TemplateView):
    template_name = "index.html"


class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('sector_list')


class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('/')


class UUIDView(DetailView):
    model = Uuid
    template_name = "uuid.html"
    slug_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(centroid=Centroid('sector__contour'))


class StatView(LoginRequiredMixin, StatMixin, TemplateView):
    template_name = 'stat/stat.html'


class AssigmentsStatView(LoginRequiredMixin, AddContextGetChangesHistoryMixin,
                         ListView):
    template_name = 'stat/assignments_blank.html'
    extra_context = {
        'header': _('Sector assignments status'),
    }
    queryset = Sector.objects.select_related("status").order_by('name')
    # .prefetch_related(
    #     Prefetch(
    #         'historical',
    #         # queryset=Sector.history.all(),
    #         # select_related('history_user', 'status'),
    #         # to_attr='history_test'
    #     )
    # )[:1]

# qs = Sector.history.
