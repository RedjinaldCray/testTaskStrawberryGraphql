from sqlalchemy import insert, select, and_
from models import User, Movie, Favorite
from sqlalchemy.engine import create_engine
from models.base import DBSession
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////Users/aleksandrchaika/Freelance/testTaskStrawberryGraphql/database.db', echo=True)
session_factory = sessionmaker(bind=engine)
db_session = DBSession(session_factory())


def like_movie(user: User, movie: Movie) -> bool:
    favorite_user_query_movie = select(Favorite).where(and_(Favorite.user == user.id, Movie.id == movie.id))
    favorite_movie_is_have = engine.execute(favorite_user_query_movie).fetchall()
    if not favorite_movie_is_have:
        insert_favorite = insert(Favorite).values(user=user.id, movie=movie.id)
        engine.execute(insert_favorite)
        return True
    return False


def get_list_favorite_movies(user: User) -> list:
    favorite_user_query = select(Favorite).where(Favorite.user == user.id)
    list_favorite = engine.execute(favorite_user_query).fetchall()
    list_movies = []
    for favorite in list_favorite:
        movie_query = select(Movie).where(Movie.id == favorite.movie)
        movie = engine.execute(movie_query).fetchone()
        list_movies.append(movie)

    return list_movies
