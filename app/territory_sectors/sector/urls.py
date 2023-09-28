from django.urls import path
from .views import SectorListView, SectorCreateView, \
    SectorDeleteView, SectorUpdateView, SectorStatusHistory, \
    SectorCheckInOutView, SectorDeptorsListView
from .viewPDFprint import SectorPrintPDF

urlpatterns = [
    path('for-serve', SectorListView.as_view(
        extra_context={'status': 'for-serve'},
    ), name='sector_list_serve'),
    path('for-search', SectorListView.as_view(
        extra_context={'status': 'for-search'},
    ), name='sector_list_search'),
    path('debtors', SectorDeptorsListView.as_view(), name='debtors'),
    path('', SectorListView.as_view(), name='sector_list'),
    path('create/', SectorCreateView.as_view(), name='sector_add'),
    path('<int:pk>/', SectorUpdateView.as_view(), name='sector_update'),
    path('<int:pk>/checkinout/', SectorCheckInOutView.as_view(),
         name='sector_checkinout'),
    path('<int:pk>/print/', SectorPrintPDF.as_view(),
         name='sector_print'),
    path('<int:pk>/delete/', SectorDeleteView.as_view(),
         name='sector_delete'),
    path('<int:pk>/history/', SectorStatusHistory.as_view(),
         name="sector_history")
]
