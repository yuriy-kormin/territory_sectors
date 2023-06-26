import graphene
from django.urls import reverse_lazy
from graphene_django import DjangoObjectType

from territory_sectors.house.models import House


class HouseNode(DjangoObjectType):
    update_href = graphene.String()
    flat_count = graphene.Int()

    class Meta:
        model = House
        fields = '__all__'

    def resolve_update_href(self, info):
        return reverse_lazy('house_update', kwargs={'pk': self.id})

    def resolve_flat_count(self, info):
        return self.flat_count()
