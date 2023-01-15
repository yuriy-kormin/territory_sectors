from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('root')


class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('/')

