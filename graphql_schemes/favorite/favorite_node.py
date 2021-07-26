import strawberry
from typing import List
from graphql_schemes.user import UserNode
from graphql_schemes.movie import MovieNode


@strawberry.type
class FavoriteNode:
    user: UserNode
    movies: List[MovieNode]
