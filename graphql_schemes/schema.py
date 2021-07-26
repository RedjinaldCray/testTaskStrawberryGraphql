import strawberry
from typing import List
from graphql_schemes.user import AuthenticationNode
from graphql_schemes.movie import MovieNode
from graphql_schemes.user import UserNode, RegistrationNode, LikeMovieNode
from graphql_schemes.favorite import FavoriteNode
from graphql_schemes.user import (
    registration_user,
    authentication_user,
    get_me,
    like_movie_mutation,
    get_my_favorite
)
from graphql_schemes.movie import get_movies


@strawberry.type
class Query:
    get_me: UserNode = strawberry.field(resolver=get_me)
    get_movies: List[MovieNode] = strawberry.field(resolver=get_movies)
    get_my_favorite: FavoriteNode = strawberry.field(resolver=get_my_favorite)


@strawberry.type
class Mutation:
    registration_user: RegistrationNode = strawberry.mutation(resolver=registration_user)
    authentication_user: AuthenticationNode = strawberry.mutation(resolver=authentication_user)
    like_movie: LikeMovieNode = strawberry.mutation(resolver=like_movie_mutation)

