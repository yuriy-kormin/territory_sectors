from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView


class FlatCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    form_class = FlatForm
    template_name = "flat/create.html"
    success_url = reverse_lazy('flat_list')
    login_url = reverse_lazy("user_login")
    extra_context = {
        'header': _('Create flat'),
        'button_title': _('Create'),
    }
    success_message = _('Flat created successfully')
