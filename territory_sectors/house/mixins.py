from django.core.paginator import Paginator
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


# class LanguagesListMixin:
#     def get_con(self):
#         qs = super(CountFlatsMixin, self).get_queryset()
#         return qs.annotate(Count('flat'))
class PaginateMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        context['page_obj'] = page_obj
        return context
