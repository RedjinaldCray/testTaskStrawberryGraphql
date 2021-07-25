from django.contrib.auth.hashers import make_password, check_password
from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'User'

    username = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    first_name = Column(VARCHAR(255), nullable=False, default="")
    movies = relationship("FavoriteMovie")

    def __repr__(self):
        return f'{self.username}'

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return check_password(password=self.password, encoded=password)
