from .get_me_query import get_me
from sql import get_movie, like_movie, get_user


def like_movie_mutation(token: str, movie_id: int) -> bool:
    check_user = get_me(token=token)
    if check_user.username != "":
        user = get_user(email=check_user.email)
        movie = get_movie(id_movie=movie_id)
        if movie is not None:
            like_movie(user=user, movie=movie)
            return True
    return False
