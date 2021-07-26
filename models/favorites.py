from .base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey


class Favorite(BaseModel):
    __tablename__ = 'FavoriteMovie'

    user = Column(Integer, ForeignKey('User.id', ondelete='CASCADE'))
    movie = Column(Integer, ForeignKey('Movie.id', ondelete='CASCADE'))
