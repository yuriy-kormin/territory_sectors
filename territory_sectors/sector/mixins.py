from django.db.models import Count


class CountHousesFlatsMixin:
    def get_queryset(self):
        qs = super(CountHousesFlatsMixin, self).get_queryset()
        return qs.annotate(Count('house'), Count('house__flat'))
