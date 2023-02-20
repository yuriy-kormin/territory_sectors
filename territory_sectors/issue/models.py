from django.conf import settings

from django.db import models


class Issue(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=3000, null=False, blank=False)
    text = models.CharField(max_length=3000, null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=3000, null=True, blank=True)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # def form_valid(self, form):
    #     form.instance.issue_id = self.kwargs['pk']
    #     form.instance.author_id = self.request.user.id
    #     return super().form_valid(form)

    # def form_valid(self, commit=True, **kwargs):
    #     comment = super().save(commit=False)
    #     raise ValueError('qq')
    #     comment.issue_id = kwargs['issue_id']
    #     comment.author_id = self.request.user.id
    #     if commit:
    #         comment.save()
    #     return comment