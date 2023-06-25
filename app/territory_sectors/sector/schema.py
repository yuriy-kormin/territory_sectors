import graphene
from graphene_django import DjangoObjectType
from .models import Sector


class SectorType(DjangoObjectType):
    class Meta:
        model = Sector
        exclude = 'contour',


class Query(graphene.ObjectType):
    sector_listing = graphene.List(SectorType)
    sector_by_id = graphene.Field(SectorType, id=graphene.Int())

    def resolve_sector_listing(self, info):
        return Sector.objects.all()

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
