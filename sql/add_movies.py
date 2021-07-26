from models import Movie
from sqlalchemy import insert
from sqlalchemy.engine import create_engine
from models.base import DBSession
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:////Users/aleksandrchaika/Freelance/testTaskStrawberryGraphql/database.db', echo=True)
session_factory = sessionmaker(bind=engine)
db_session = DBSession(session_factory())


movies_list = [
    {
        "name": "Солнечное затмение",
        "desc": "Фильм о явлении в природе, повествует о солнечном затмении в 2022"
    },
    {
        "name": "Легенда",
        "desc": "Повесть о двух гангстерах бротев Ренджинальда и Ронни Креев, которые берут под себя всю Англию "
                "30 годов"
    },
    {
        "name": "Тренер",
        "desc": "Фильм о тренере сборной команды Noname, котоыре выигрывают чемпионат России"
    }
]


def add_movie():
    for movie in movies_list:
        print(movie)
        result = insert(Movie).values(name=movie['name'], description=movie['desc'])
        engine.execute(result)


if __name__ == '__main__':
    add_movie()
