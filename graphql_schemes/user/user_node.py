import strawberry


@strawberry.type
class UserNode:
    username: str
    email: str
    first_name: str
    password: str = None
