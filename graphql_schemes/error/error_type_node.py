import strawberry


@strawberry.type
class ErrorNode:
    error: bool = False
    message: str = ""
