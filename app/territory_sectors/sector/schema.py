import graphene
from django.urls import reverse_lazy
from graphene_django import DjangoObjectType
from graphene_gis.converter import gis_converter  # noqa
from .models import Sector
from ..status.models import Status
from ..house.models import House


class StatusType(DjangoObjectType):
    class Meta:
        model = Status
        fields = 'name',


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


class SectorNode(DjangoObjectType):
    status = graphene.String()
    contour = graphene.JSONString()
    uuid = graphene.String()
    update_href = graphene.String()
    history_href = graphene.String()
    remove_href = graphene.String()
    houses = graphene.List(HouseNode)

    class Meta:
        model = Sector
        fields = '__all__'

    def resolve_status(self, info):
        return getattr(self.status, 'name', None)

    def resolve_update_href(self, info):
        return reverse_lazy('sector_update', kwargs={'pk': self.id})

    def resolve_history_href(self, info):
        return reverse_lazy('sector_history', kwargs={'pk': self.id})

    def resolve_remove_href(self, info):
        return reverse_lazy('sector_delete', kwargs={'pk': self.id})

    def resolve_houses(self, info):
        return self.get_houses_into()


class Query(graphene.ObjectType):
    sector_listing = graphene.List(SectorNode)
    sector_by_id = graphene.Field(SectorNode, id=graphene.Int())

    def resolve_sector_listing(self, info):
        return Sector.objects.select_related('status', 'uuid')\
            .order_by('status__id')

    def resolve_sector_by_id(self, info, id):
        return Sector.objects.get(id=id)

# class Mutation(graphene.Mutation):
#     # class Arguments:
#     #     name = graphene.String()
#     #     phone_number = graphene.String()
#
#     # contact = graphene.Field(SectorType)
#     def mutate(cls, root, info, name, phone_number):
#       pass
