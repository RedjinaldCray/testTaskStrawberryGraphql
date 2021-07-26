import strawberry
from graphql_schemes.error import ErrorNode


@strawberry.type
class AuthenticationNode:
    token: str
    error: ErrorNode = None
