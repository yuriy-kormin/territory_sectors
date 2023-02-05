from django.urls import path
from .views import SectorListView, SectorCreateView,\
    SectorDeleteView, SectorUpdateView

urlpatterns = [
    path('', SectorListView.as_view(), name='sector_list'),
    path('create/', SectorCreateView.as_view(), name='sector_add'),
    path('<int:pk>/', SectorUpdateView.as_view(), name='sector_update'),
    path('<int:pk>/delete/', SectorDeleteView.as_view(),
         name='sector_delete'),
]
