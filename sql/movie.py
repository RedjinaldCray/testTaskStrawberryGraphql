from models import Movie
from sqlalchemy import select
from sqlalchemy.engine import create_engine
from models.base import DBSession
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////Users/aleksandrchaika/Freelance/testTaskStrawberryGraphql/database.db', echo=True)
session_factory = sessionmaker(bind=engine)
db_session = DBSession(session_factory())


def get_movies_list() -> list:
    get_movie_query = select(Movie)
    movies = engine.execute(get_movie_query).fetchall()
    print('movies', movies)

    return movies


def get_movie(id_movie: int) -> Movie or None:
    get_movie_query = select(Movie).where(Movie.id == id_movie)
    movie = engine.execute(get_movie_query).fetchall()

    if movie:
        return movie[0]
    return None
