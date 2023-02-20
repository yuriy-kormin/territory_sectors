from django.urls import path
from .views import IssueListView,IssueCreateView,IssueDetailView,CommentCreateView

urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('create/', IssueCreateView.as_view(), name='issue_add'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('comment/<int:pk>', CommentCreateView.as_view(), name='comment_create'),
]
