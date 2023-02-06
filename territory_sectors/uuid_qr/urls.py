from django.urls import path
from .views import gen_qr

urlpatterns = [
    path('gen', gen_qr, name='uuid_gen'),
    # path('create/', FlatCreateView.as_view(), name='flat_add'),
    # path('<int:pk>/', FlatUpdateView.as_view(), name='flat_update'),
    # path('<int:pk>/delete/', FlatDeleteView.as_view(), name='flat_delete'),
]
