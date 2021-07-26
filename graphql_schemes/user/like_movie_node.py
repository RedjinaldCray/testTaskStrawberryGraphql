import strawberry
from graphql_schemes.error import ErrorNode


@strawberry.type
class LikeMovieNode:
    like: bool
    error: ErrorNode = None
