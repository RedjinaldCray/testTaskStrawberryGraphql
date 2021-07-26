import strawberry
from typing import List
from .movie import MovieNode
from .user import UserNode
from .token_node import Token
from graphql_schemes.user import registration_user, authentication_user, get_me, like_movie_mutation
from graphql_schemes.movie import get_movies


@strawberry.type
class Query:
    get_me: UserNode = strawberry.field(resolver=get_me)
    get_movies: List[MovieNode] = strawberry.field(resolver=get_movies)


@strawberry.type
class Mutation:
    registration_user: bool = strawberry.mutation(resolver=registration_user)
    authentication_user: Token = strawberry.mutation(resolver=authentication_user)
    like_movie: bool = strawberry.mutation(resolver=like_movie_mutation)

