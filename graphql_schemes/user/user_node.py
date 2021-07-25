import strawberry


@strawberry.type
class User:
    username: str
    email: str
    password: str
    first_name: str
