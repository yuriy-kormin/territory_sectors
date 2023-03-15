from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .forms import StatusForm
from .models import Status
from django.utils.translation import gettext_lazy as _


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "status/list.html"
    extra_context = {
        'header': _('List statuses'),
    }


class StatusCreateView(LoginRequiredMixin,
                       SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = "issue/create.html"
    success_url = reverse_lazy("status_list")
    login_url = reverse_lazy("user_login")
    extra_context = {
        'header': _('Create status'),
        'button_title': _('Create'),
    }
    success_message = _('Status created successfully')


class StatusUpdateView(LoginRequiredMixin,
                       SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "issue/create.html"
    success_url = reverse_lazy("status_list")
    login_url = reverse_lazy("user_login")
    extra_context = {
        'header': _('Update status'),
        'button_title': _('Update'),
    }
    success_message = _('Status updated successfully')
