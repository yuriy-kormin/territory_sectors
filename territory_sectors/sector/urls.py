from django.urls import path
from .views import SectorListView, SectorCreateView,\
    SectorDeleteView, SectorUpdateView, SectorStatusHistory, SectorPrintView

urlpatterns = [
    path('', SectorListView.as_view(), name='sector_list'),
    path('create/', SectorCreateView.as_view(), name='sector_add'),
    path('<int:pk>/', SectorUpdateView.as_view(), name='sector_update'),
    path('<int:pk>/print/', SectorPrintView.as_view(),
         name='sector_print'),
    path('<int:pk>/delete/', SectorDeleteView.as_view(),
         name='sector_delete'),
    path('<int:pk>/history/', SectorStatusHistory.as_view(),
         name="sector_history")
]
