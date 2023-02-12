# from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Uuid


# Create your views here.
def gen_qr(request):
    Uuid.objects.create()
    return redirect(reverse_lazy('root'))
