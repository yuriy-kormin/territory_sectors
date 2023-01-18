from django.urls import path
from .views import HouseListView, HouseCreateView, HouseUpdateView, HouseDeleteView

urlpatterns = [
    path('', HouseListView.as_view(), name='house_list'),
    path('create/', HouseCreateView.as_view(), name='house_add'),
    path('<int:pk>/', HouseUpdateView.as_view(), name='house_update'),
    path('<int:pk>/delete/', HouseDeleteView.as_view(), name='house_delete'),
]
