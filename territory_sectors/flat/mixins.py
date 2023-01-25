from django.db.models import Count
from django.shortcuts import redirect

from .models import Flat
from territory_sectors.house.models import House
from django.views.generic.list import MultipleObjectMixin


class HousesAddMixin(MultipleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['houses'] = House.objects.filter(
            flat__in=self.get_queryset()
        ).annotate(Count('flat'))

        return context


class SeveralInstanceCreateMixin:
    def form_valid(self, form):
        def separate(string):
            if ',' in string:
                return [i for i in string.split(',') if len(i)]

        if numbers := separate(form.instance.number):
            instances = []
            for num in numbers:
                instances.append(
                    Flat(
                        house=form.instance.house,
                        entrance=form.instance.entrance,
                        floor=form.instance.floor,
                        way_desc=form.instance.way_desc,
                        language=form.instance.language,
                        number=num
                    )
                )
            Flat.objects.bulk_create(instances)
            return redirect(self.get_success_url())
        return super().form_valid(form)

#
# class HouseListMixin(Multi):
#     def get_queryset(self):
#         qs = super(CountFlatsMixin, self).get_queryset()
#         return qs.annotate(Count('flat'))
# def get_context_data(self, **kwargs):
#     query = self.get_queryset()
#     context = super().get_context_data(**kwargs)
#     obj = self.model
#     context[object] = House.objects.filter(
#         flat__in=query
#     ).distinct().annotate(Count('flat'))
#
#     return context
