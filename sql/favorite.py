import logging

from sqlalchemy import insert
from models import User, Movie, Favorite
from sqlalchemy.engine import create_engine
from models.base import DBSession
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////Users/aleksandrchaika/Freelance/testTaskStrawberryGraphql/database.db', echo=True)
session_factory = sessionmaker(bind=engine)
db_session = DBSession(session_factory())


def like_movie(user: User, movie: Movie) -> bool:
    try:
        insert_favorite = insert(Favorite).values(user=user.id, movie=movie.id)
        engine.execute(insert_favorite)

        return True
    except Exception as e:
        print(e)
        return False
