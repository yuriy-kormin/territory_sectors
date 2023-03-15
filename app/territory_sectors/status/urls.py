from django.urls import path
from .views import StatusListView, StatusCreateView, StatusUpdateView

# StatusCreateView, StatusUpdateView

urlpatterns = [
    path('', StatusListView.as_view(), name='status_list'),
    path('create/', StatusCreateView.as_view(), name='status_add'),
    path('<int:pk>/', StatusUpdateView.as_view(), name='status_update'),
]
