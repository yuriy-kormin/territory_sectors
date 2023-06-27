import re

import graphene
from django.urls import reverse_lazy
from graphene_django import DjangoObjectType
from django.template.loader import render_to_string

from territory_sectors.house.models import House


class HouseNode(DjangoObjectType):
    update_href = graphene.String()
    flat_count = graphene.Int()
    popup = graphene.String()

    class Meta:
        model = House
        fields = '__all__'

    def resolve_update_href(self, info):
        return reverse_lazy('house_update', kwargs={'pk': self.id})

    def resolve_flat_count(self, info):
        return self.flat_count()

    def resolve_popup(self, info):
        return re.sub(
            r'\s{2}',
            '',
            render_to_string(
                'house/house_popup.html',
                {'house': House.objects.get(pk=self.id)}
            )
        )


class Query(graphene.ObjectType):
    house_listing = graphene.List(HouseNode)
    house_by_id = graphene.Field(HouseNode, id=graphene.Int())

    def resolve_house_listing(self, info):
        return House.objects.all()

    def resolve_house_by_id(self, info, id):
        return House.objects.get(pk=id)
