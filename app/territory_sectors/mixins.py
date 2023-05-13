from urllib.parse import urlparse

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .house.models import House
from .sector.models import Sector
from .flat.models import Flat


class SetAuthorMixin:
    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.id)
        form.instance.author = user
        return super().form_valid(form)


class LoginRequiredMixinCustom(LoginRequiredMixin):
    login_url = reverse_lazy('user_login')
    permission_denied_message = _("Please login to access this page")

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())
        # If the login url is the same scheme and net location then use the
        # path as the "next" url.
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
                not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()
        return redirect_to_login(
            path,
            resolved_login_url,
            self.get_redirect_field_name(),
        )


class StatMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_houses'] = House.stat.total_count()
        context['total_flats'] = Flat.stat.total_count()
        context['total_ru_flats'] = Flat.stat.total_ru_count()
        context['total_non_ru_flats'] = \
            context['total_flats'] - context['total_ru_flats']
        context['total_sectors'] = Sector.stat.total_count()
        context['sector_free'] = Sector.stat.free_count()
        context['sector_assigned'] = Sector.stat.assigned_count()
        context['sector_completed'] = Sector.stat.completed_count()

        return context
