import graphene
from graphene_django import DjangoObjectType
from .models import Uuid


class UuidNode(DjangoObjectType):
    ok = graphene.Boolean()

    class Meta:
        model = Uuid
        fields = None


class Query(graphene.ObjectType):
    uuid_check = graphene.Field(UuidNode, id=graphene.String())

    def resolve_uuid_check(self, info, id):
        instances = Uuid.objects.filter(id=id)
        uuid_sector = getattr(instances[0], 'sector', None)
        if instances and uuid_sector:
            return UuidNode(ok=True)
        return UuidNode(ok=False)
