from graphene_django import DjangoObjectType

from territory_sectors.status.models import Status


class StatusNode(DjangoObjectType):
    class Meta:
        model = Status
        fields = 'name',
