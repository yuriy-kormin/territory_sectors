from django.urls import path
from .views import FlatListView, FlatCreateView, FlatUpdateView, FlatDeleteView

urlpatterns = [
    path('', FlatListView.as_view(), name='flat_list'),
    path('create/', FlatCreateView.as_view(), name='flat_add'),
    path('<int:pk>/', FlatUpdateView.as_view(), name='flat_update'),
    path('<int:pk>/delete/', FlatDeleteView.as_view(), name='flat_delete'),
]
