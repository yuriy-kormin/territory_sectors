from django.urls import path
from .views import HouseListView, HouseCreateView, HouseDetailView

urlpatterns = [
    path('', HouseListView.as_view(), name='house_list'),
    path('create/', HouseCreateView.as_view(), name='house_add'),
    path('<int:pk>/', HouseDetailView.as_view(), name='house_view'),
    # path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    # path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]
