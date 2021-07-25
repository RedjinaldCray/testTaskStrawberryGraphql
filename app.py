from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from graphql_schemes import Query, Mutation
import strawberry
import os
from models.base import DBSession, BaseModel

engine = create_engine('sqlite:///database.db', echo=True)
if not os.path.exists(path='database.db'):
    BaseModel.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
db_session = DBSession(session_factory())

schema = strawberry.Schema(query=Query, mutation=Mutation)
