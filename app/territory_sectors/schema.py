import graphene
from territory_sectors.sector.schema import Query as SectorQuery
from territory_sectors.house.schema import Query as HouseQuery


class Query(
    SectorQuery,
    HouseQuery,
):
    pass


# class Mutation(
#     # StatusMutation,
# ):
#     pass


schema = graphene.Schema(query=Query)
# , mutation=Mutation)
