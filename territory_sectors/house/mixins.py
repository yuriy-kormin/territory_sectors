from django.db.models import Count


class CountFlatsMixin:
    def get_queryset(self):
        qs = super(CountFlatsMixin, self).get_queryset()
        return qs.annotate(Count('flat'))
    # def get_context_data(self, **kwargs):
    #     query = self.get_queryset()
    #     context = super().get_context_data(**kwargs)
    #     obj = self.model
    #     context[object] = House.objects.filter(
    #         flat__in=query
    #     ).distinct().annotate(Count('flat'))
    #
    #     return context
