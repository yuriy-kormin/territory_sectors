from django.conf import settings
from django.contrib.auth.models import User


class SetAuthorMixin:
    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.id)
        form.instance.author = user
        return super().form_valid(form)
