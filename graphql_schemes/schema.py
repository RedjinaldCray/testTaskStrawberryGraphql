import strawberry
from .user import user_node
from .token_node import Token
from graphql_schemes.user import registration_user, authentication_user, get_me


@strawberry.type
class Query:
    get_me: user_node = strawberry.field(resolver=get_me)


@strawberry.type
class Mutation:
    registration_user: bool = strawberry.mutation(resolver=registration_user)
    authentication_user: Token = strawberry.mutation(resolver=authentication_user)

