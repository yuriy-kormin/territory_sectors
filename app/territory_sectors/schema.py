import graphene
from territory_sectors.sector.schema import Query as SectorQuery
from territory_sectors.house.schema import Query as HouseQuery
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


class Query(
    SectorQuery,
    HouseQuery,
):
    pass


class Mutation(
    AuthMutation,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
