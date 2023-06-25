import graphene
from territory_sectors.sector.schema import Query as SectorQuery


class Query(
    SectorQuery,
):
    pass


# class Mutation(
#     # StatusMutation,
# ):
#     pass


schema = graphene.Schema(query=Query)
# , mutation=Mutation)
