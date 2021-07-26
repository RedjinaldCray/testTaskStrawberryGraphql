from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, VARCHAR
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'User'

    username = Column(VARCHAR(255), nullable=False, unique=True)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    password = Column(VARCHAR(255), nullable=False)
    first_name = Column(VARCHAR(255), nullable=False, default="")

    def __repr__(self):
        return f'{self.username}'

    @staticmethod
    def set_password(password: str) -> str:
        password = generate_password_hash(password)

        return password

    @staticmethod
    def check_password(password: str, hash_password: str) -> bool:
        return check_password_hash(hash_password, password)
