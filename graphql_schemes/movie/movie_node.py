import strawberry


@strawberry.type
class MovieNode:
    id: int
    name: str
    description: str
