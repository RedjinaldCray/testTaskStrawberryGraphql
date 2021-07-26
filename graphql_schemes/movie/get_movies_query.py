from sql import get_movies_list
from typing import List
from ..movie.movie_node import MovieNode


def get_movies() -> List[MovieNode]:
    movies_list = get_movies_list()
    return movies_list
