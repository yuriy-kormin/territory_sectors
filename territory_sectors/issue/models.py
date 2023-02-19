from django.db import models


class Issue(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=3000, null=False, blank=False)
    message = models.CharField(max_length=3000, null=True, blank=True)


class Comment(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=3000, null=True, blank=True)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
