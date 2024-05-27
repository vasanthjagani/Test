import graphene
from base.schema import BaseQuery, BaseMutation


class Query(BaseQuery, graphene.ObjectType,):
    pass


class Mutation(BaseMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
