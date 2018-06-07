import graphene
import graphql_jwt

import usuarios.schema
import amigos.schema
import mensajes.schema


class Query(usuarios.schema.Query, amigos.schema.Query, mensajes.schema.Query, graphene.ObjectType):
    pass


class Mutation(usuarios.schema.Mutation, amigos.schema.Mutation, mensajes.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
