import strawberry
from sql import create_user, username_is_already, email_is_already
from models import User
from graphql_schemes.user import registration_user, authentication_user


@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: str = "World") -> str:
        return f"Hello {name}"


@strawberry.type
class Mutation:
    registration_user: bool = strawberry.mutation(resolver=registration_user)
    authentication_user: str = strawberry.mutation(resolver=authentication_user)

