import strawberry
from graphql_schemes.error import ErrorNode


@strawberry.type
class RegistrationNode:
    registration: bool
    error: ErrorNode = None
