from django.urls import path
from .views import IssueListView,IssueCreateView,IssueDetailView

urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('create/', IssueCreateView.as_view(), name='issue_add'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
]
