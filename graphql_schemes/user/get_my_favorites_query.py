from ..favorite.favorite_node import FavoriteNode
from ..user.get_me_query import get_me
from sql import get_user, get_list_favorite_movies


def get_my_favorite(token: str) -> FavoriteNode:
    check_user = get_me(token=token)
    if check_user.username != "":
        user = get_user(email=check_user.email)
        if user is not None:
            list_favorite_movies = get_list_favorite_movies(user=user)
            return FavoriteNode(user=check_user, movies=list_favorite_movies)

    return FavoriteNode(user=check_user, movies=[])
