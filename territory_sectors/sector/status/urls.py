from django.urls import path
from .views import StatusSectorListView, StatusSectorCreateView,\
    StatusSectorDeleteView, StatusSectorUpdateView

urlpatterns = [

    path('', StatusSectorListView.as_view(),
         name='status_sector_list'),
    path('create/', StatusSectorCreateView.as_view(),
         name='status_sector_add'),
    path('<int:pk>/', StatusSectorUpdateView.as_view(),
         name='status_sector_update'),
    path('<int:pk>/delete/', StatusSectorDeleteView.as_view(),
         name='status_sector_delete'),

]
