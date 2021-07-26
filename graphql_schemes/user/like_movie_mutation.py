from graphql_schemes.user import LikeMovieNode
from graphql_schemes.error import ErrorNode
from graphql_schemes.user import get_me
from sql import get_movie, like_movie, get_user


def like_movie_mutation(token: str, movie_id: int) -> LikeMovieNode:
    text = ""
    error = False
    like = False
    check_user = get_me(token=token)
    if check_user.username != "":
        user = get_user(email=check_user.email)
        if user is not None:
            movie = get_movie(id_movie=movie_id)
            if movie is not None:
                like = like_movie(user=user, movie=movie)
            else:
                text = "Movie not found"
        else:
            text = "User not found"
    else:
        text = "User not found"

    if text != "":
        error = True

    return LikeMovieNode(like=like, error=ErrorNode(error=error, message=text))
