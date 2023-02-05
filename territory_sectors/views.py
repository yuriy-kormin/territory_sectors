# import shortuuid
from django.db.models import Count
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from territory_sectors.uuid_qr.models import Uuid


# from territory_sectors.sector.mixins import GeoJSONAnnotateMixin


class IndexView(TemplateView):
    template_name = "index.html"


class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('root')


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
        return qs.annotate(
            flat_count=Count('sector__house__flat')
        )
    #
    # def get_object(self, queryset=None):
    #     uuid = self.kwargs.get('uuid')
    #     # id = shortuuid.decode(uuid)
    #     return self.model.objects.get(id=uuid)
