from django.urls import path
from .views import FlatListView, FlatCreateView, FlatDetailView

urlpatterns = [
    path('', FlatListView.as_view(), name='flat_list'),
    path('create/', FlatCreateView.as_view(), name='flat_add'),
    path('<int:pk>/', FlatDetailView.as_view(), name='flat_view'),
    # path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    # path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]
