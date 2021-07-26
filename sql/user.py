from models import User
from sqlalchemy import insert, select
from sqlalchemy.engine import create_engine
from models.base import DBSession
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
session_factory = sessionmaker(bind=engine)
db_session = DBSession(session_factory())


def create_user(username: str, password: str, email: str, first_name: str) -> User:
    result = insert(User).values(username=username, password=password, email=email, first_name=first_name)
    engine.execute(result)
    user = db_session.query(User).filter(User.username == username).one()

    return user


def username_is_already(username: str) -> bool:
    get_user_query = select(User).where(User.username == username)
    user = engine.execute(get_user_query).fetchall()
    if user:
        return True
    return False


def email_is_already(email: str) -> bool:
    get_user_query = select(User).where(User.email == email)
    user = engine.execute(get_user_query).fetchall()
    if user:
        return True
    return False


def check_password(password: str, email: str) -> bool:
    if email_is_already(email=email):
        get_user_query = select(User).where(User.email == email)
    elif username_is_already(username=email):
        get_user_query = select(User).where(User.username == email)
    else:
        return False
    user = engine.execute(get_user_query).fetchall()[0]

    return User.check_password(password=password, hash_password=user.password)


def get_user(email: str) -> User or None:
    get_user_query = select(User).where(User.email == email)
    user = engine.execute(get_user_query).fetchall()
    if user:
        return user[0]

    return None


def get_user_by_username(username: str) -> User or None:
    get_user_query = select(User).where(User.username == username)
    user = engine.execute(get_user_query).fetchall()
    if user:
        return user[0]

    return None


def check_hash_password(hash_password: str, email: str) -> bool:
    user = get_user(email=email)
    if user is not None:
        if hash_password == user.password:
            return True
    return False
