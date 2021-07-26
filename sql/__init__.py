from .user import create_user, username_is_already, email_is_already, check_password, get_user, check_hash_password
from sqlalchemy.engine import create_engine
from models.base import DBSession
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
session_factory = sessionmaker(bind=engine)
db_session = DBSession(session_factory())
