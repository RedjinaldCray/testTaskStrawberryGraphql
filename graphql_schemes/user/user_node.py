import strawberry
from typing import Any


@strawberry.type
class User:
    username: str
    email: str
    first_name: str
    password: str = None
