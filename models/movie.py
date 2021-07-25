from .base import BaseModel
from sqlalchemy import Column, VARCHAR


class Movie(BaseModel):
    __tablename__ = 'Movie'

    name = Column(VARCHAR(255), nullable=False)
    description = Column(VARCHAR(2048), nullable=False, default="")
