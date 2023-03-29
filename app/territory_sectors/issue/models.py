from django.conf import settings

from django.db import models


class Issue(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=3000, null=False, blank=False)
    text = models.CharField(max_length=3000, null=True, blank=True)
    completed = models.BooleanField(
        default=False,
        help_text='check if task is completed.Uncheck, if task need to improve',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = 'date',


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=3000, null=True, blank=True)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
