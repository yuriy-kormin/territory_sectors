from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.utils.translation import gettext_lazy as _

from .forms import IssueForm, CommentForm
from .mixins import SetAuthorMixin
from .models import Issue, Comment


class IssueCreateView(LoginRequiredMixin, SetAuthorMixin,
                      SuccessMessageMixin, CreateView):
    form_class = IssueForm
    template_name = "issue/create.html"
    success_url = reverse_lazy("issue_list")
    login_url = reverse_lazy("user_login")
    extra_context = {
        'header': _('Create issue'),
        'button_title': _('Create'),
    }
    success_message = _('Issue created successfully')


class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = "issue/list.html"
    extra_context = {
        'header': _('List issues'),
    }


# class CommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'comment_form.html'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         form.instance.issue_id = self.kwargs['pk']
#         return super().form_valid(form)
#


class IssueDetailView(LoginRequiredMixin, SetAuthorMixin, DetailView):
    model = Issue
    template_name = "issue/detail.html"
    extra_context = {
        'header': _('Issue detail'),
        'button_title': _('Comment'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(issue_id=context['issue'])
        context['new_comment'] = CommentForm()
        return context


class CommentCreateView(SuccessMessageMixin, CreateView):
    success_message = _("Comment added")
    model = Comment
    form_class = CommentForm
    template_name = 'issue/comment_form.html'
    success_url = reverse_lazy('issue_list')

    def form_valid(self, form):
        form.instance.issue_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        form.instance.save()
        return super().form_valid(form)
